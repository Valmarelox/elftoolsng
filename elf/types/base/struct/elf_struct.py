import struct

from elf.types.base.struct.elf_meta import ElfMeta
from elf.types.base import ElfOffset
from elf.types.base import ElfTypeBase
from elf.types.base.int import ElfInt32Type
from elf.types.base.int import ElfInt64Type
from elf.types.base.int import ElfIntNType
from elf.types.base.struct import ElfStructProperty
from pprint import pformat


class ElfStruct(ElfTypeBase, metaclass=ElfMeta):
    PROPERTIES: [ElfStructProperty] = []

    def read(self):
        return struct.unpack(self.format, self.data)

    def write(self, *args):
        self.elf.raw_write(self.offset, struct.pack(self.format, *args))

    @property
    def format(self):
        f = '<' + ''.join(prop.type.STRUCT for prop in self.PROPERTIES)
        if self.elf.is64bit:
            return f.replace(ElfIntNType.STRUCT, ElfInt64Type.STRUCT)
        else:
            return f.replace(ElfIntNType.STRUCT, ElfInt32Type.STRUCT)

    def __repr__(self):
        return pformat({'name': type(self).__name__,
                        'fields': [{prop.name: getattr(self, prop.name)} for prop in self.PROPERTIES]})

    @classmethod
    def size(cls):
        return sum((prop.type.size() for prop in cls.PROPERTIES), ElfOffset())

    @property
    def data(self):
        return self.raw