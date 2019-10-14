import struct
from types import MethodType
import types
from functools import wraps
from typing import Dict, Any


class ElfStructProperty(object):
    def __init__(self, name, index):
        super(ElfStructProperty, self).__init__()
        self.name = name
        self.index = index


class ElfMeta(type):

    def __call__(self, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)

        def make_generic_getter(index):
            def _generic_getter(self):
                return self.read()[index]

            return _generic_getter

        def make_generic_setter(index):
            def _generic_setter(self, data):
                read = list(self.read())
                read[index] = data
                return self.write(*read)

            return _generic_setter

        for index, prop in enumerate(obj.PROPERTIES):
            getter = make_generic_getter(index)
            setter = make_generic_setter(index)
            #setattr(obj, '__' + prop + '_get', getter)
            #setattr(obj, '__' + prop + '_set', setter)
            setattr(obj, prop, property(MethodType(getter, obj),
                                        MethodType(setter, obj)))

        return obj


class ElfStruct(object, metaclass=ElfMeta):
    FORMAT = ''
    IS_ELF64 = None
    PROPERTIES: [str] = []

    def __init__(self, elf):
        """

        :type elf: ELF
        """
        super().__init__()
        self.elf = elf

    @property
    def data(self):
        return self.elf.raw_read(0, self.size())

    def read(self):
        return struct.unpack(self.format(), self.data)

    def write(self, *args):
        return struct.pack(self.format(), *args)

    @classmethod
    def format(cls):
        if cls.is_elf64():
            return cls.FORMAT.replace('X', 'Q')
        else:
            return cls.FORMAT.replace('X', 'I')

    @classmethod
    def size(cls):
        return struct.calcsize(cls.format())

    @classmethod
    def is_elf64(cls):
        return cls.IS_ELF64
