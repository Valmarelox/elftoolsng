from elf.types.base.int import ElfInt32Type
from elf.types.base.elf_offset import ElfOffset


# TODO: Generify to ElfStringType
class SHName(ElfInt32Type):
    def __bytes__(self):
        return bytes(self.elf.sections[self.elf.header.e_shstrndx].section.read_string(ElfOffset(self)))

    def __eq__(self, other):
        if isinstance(other, bytes):
            return bytes(self) == other
        elif isinstance(other, SHName):
            return bytes(self) == bytes(other)
        else:
            return super().__eq__(other)

    def __str__(self):
        return str(bytes(self), 'ascii')

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if isinstance(other, bytes):
            return bytes(self) == other
        elif isinstance(other, SHName):
            return bytes(self) < bytes(other)
        else:
            return super().__eq__(other)