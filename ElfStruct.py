import struct
from types import MethodType
import types
from functools import wraps
from typing import Dict, Any


class ElfStructProperty(object):
    def __init__(self, name, type):
        super(ElfStructProperty, self).__init__()
        self.name = name
        self.type = type


class ElfTypeBase(object):
    STRUCT = ''

    def __init__(self, parent, offset):
        self.parent = parent
        self.elf = self.parent.elf
        self.offset = offset

    def raw_read(self):
        return self.elf.raw_read(self.offset, self.size())

    def raw_write(self, data):
        assert data is bytearray or data is bytes
        return self.elf.raw_write(self.offset, self.size())

    @property
    def data(self):
        x = struct.unpack(self.STRUCT, self.raw_read())
        if not self.verify(*x):
            print('Bad value in field {type}:{value}'.format(type=type(self), value=x))
        if len(x) == 1:
            x = x[0]
        return x

    def verify(self, *args):
        return True

    @data.setter
    def data(self, *args):
        if not self.verify(*args):
            assert False
        self.raw_write(struct.pack(self.STRUCT, *args))

    @classmethod
    def size(cls):
        return struct.calcsize(cls.STRUCT)


class ArchIntMetaClass(type):
    def __call__(cls, *args, **kwargs):
        parent = args[0]
        if parent.elf.is64bit:
            return ElfInt64Type(*args, **kwargs)
        else:
            return ElfInt32Type(*args, **kwargs)


class ElfIntNType(metaclass=ArchIntMetaClass):
    STRUCT = 'X'


class ElfInt8Type(ElfTypeBase):
    STRUCT = 'B'


class ElfInt16Type(ElfTypeBase):
    STRUCT = 'H'


class ElfInt32Type(ElfTypeBase):
    STRUCT = 'I'


class ElfInt64Type(ElfTypeBase):
    STRUCT = 'Q'


def ElfTypeBytes(size):
    class ElfTypeBytes(ElfTypeBase):
        STRUCT = '{}s'.format(size)
    return ElfTypeBytes


class ElfMeta(type):
    def __call__(cls, *args, **kwargs):
        def make_generic_getter(type, offset):
            def _generic_getter(self):
                return type(self, offset)

            return _generic_getter

        def make_generic_setter(type, offset):
            def _generic_setter(self, data):
                self.elf.raw_write(offset, data)

            return _generic_setter

        curr_offset = 0
        parent = args[0]
        for index, prop in enumerate(cls.PROPERTIES):
            if prop.type == ElfIntNType:
                prop.type = ElfInt64Type if parent.elf.is64bit else ElfInt32Type
            getter = make_generic_getter(prop.type, parent.offset + curr_offset)
            setter = make_generic_setter(prop.type, parent.offset + curr_offset)
            setattr(cls, prop.name, property(getter,
                                             setter))
            curr_offset += prop.type.size()

        obj = super().__call__(*args, **kwargs)
        return obj


class ElfStruct(ElfTypeBase, metaclass=ElfMeta):
    PROPERTIES: [str] = []

    def read(self):
        return struct.unpack(self.format, self.data)

    def write(self, *args):
        self.elf.raw_write(self.offset, struct.pack(self.format, *args))

    @property
    def format(self):
        f = '<' + ''.join(prop.type.STRUCT for prop in self.PROPERTIES)
        if self.elf.is64bit:
            format = f.replace(ElfIntNType.STRUCT, ElfInt64Type.STRUCT)
        else:
            format = f.replace(ElfIntNType.STRUCT, ElfInt32Type.STRUCT)
        return format
