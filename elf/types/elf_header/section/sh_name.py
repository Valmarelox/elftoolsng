from elf.types.base.int import ElfInt32Type
from elf.types.elf_offset import ElfOffset


# TODO: Generify to ElfStringType
class SHName(ElfInt32Type):
    def __bytes__(self):
        shstrtab_offset = self.elf.sections[self.elf.header.e_shstrndx].sh_offset
        offset = ElfOffset(int(shstrtab_offset) + int(self.data))
        return bytes(self.elf.raw_read_string(offset))

    def __eq__(self, other):
        if isinstance(other, bytes):
            return bytes(self) == other
        else:
            return super().__eq__(other)

    def __repr__(self):
        return bytes(self)
