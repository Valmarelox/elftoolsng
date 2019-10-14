import struct

from types.elf_meta import ElfMeta
from types.elf_type_base import ElfTypeBase
from types.int.elf_int_32_type import ElfInt32Type
from types.int.elf_int_64_type import ElfInt64Type
from types.int.elf_int_n_type import ElfIntNType


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