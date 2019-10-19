from elf.types.base.int import ElfInt32Type
from elf.types.elf_offset import ElfOffset


class SHName(ElfInt32Type):

    def __str__(self):
        shstrtab_offset = self.elf.sections[self.elf.header.e_shstrndx].sh_offset
        offset = ElfOffset(int(shstrtab_offset) + int(self.data))
        return str(self.elf.raw_read_string(offset))

    def __repr__(self):
        return str(self)
