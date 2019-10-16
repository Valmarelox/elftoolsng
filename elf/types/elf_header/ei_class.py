from elf.types.int.elf_int_8_type import ElfInt8Type


class EIClass(ElfInt8Type):
    ELFCLASSNONE = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2

    @property
    def is64bit(self):
        return self.data == self.ELFCLASS64

    def verify(self, val):
        return val in [self.ELFCLASS32, self.ELFCLASS64]