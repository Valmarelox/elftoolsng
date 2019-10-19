import struct

from elf.types.elf_offset import ElfOffset
from elf.types.elf_header.base.struct.elf_meta import ElfMeta
from elf.types.elf_type_base import ElfTypeBase
from elf.types.elf_header.base.int import ElfInt32Type
from elf.types.elf_header.base.int import ElfInt64Type
from elf.types.elf_header.base.int import ElfIntNType
from elf.types.elf_header.base.struct.elf_struct_property import ElfStructProperty
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
            format = f.replace(ElfIntNType.STRUCT, ElfInt64Type.STRUCT)
        else:
            format = f.replace(ElfIntNType.STRUCT, ElfInt32Type.STRUCT)
        return format

    def __repr__(self):
        return pformat({'name': type(self).__name__,
                        'fields': [{prop.name: getattr(self, prop.name)} for prop in self.PROPERTIES]})

    @classmethod
    def size(cls):
        return sum((prop.type.size() for prop in cls.PROPERTIES), ElfOffset())
