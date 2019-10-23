from elf.types.base.elf_name_type import ElfNameType
from elf.types.base import ElfOffset


# TODO: Generify to ElfStringType
class SHName(ElfNameType):
    @property
    def strtab_accessor(self):
        return int(self.elf.header.e_shstrndx)
