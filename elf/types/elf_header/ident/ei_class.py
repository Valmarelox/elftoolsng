from elf.types.base.int import ElfInt8Enum


class EIClass(ElfInt8Enum):
    VALS = [
        'ELFCLASSNONE',
        'ELFCLASS32',
        'ELFCLASS64',
    ]

    @property
    def is64bit(self):
        return self.data == self.ELFCLASS64
