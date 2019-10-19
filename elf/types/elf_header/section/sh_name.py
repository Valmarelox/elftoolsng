from elf.types.base.int import ElfInt32Type


class SHName(ElfInt32Type):


    def __str__(self):
        return self.elf.raw_read(self.sections)

    def __repr__(self):
        return str(self.data)