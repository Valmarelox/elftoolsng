from elf.types.base.int import ElfInt32Enum


class SHType(ElfInt32Enum):
    VALS = [
        'SHT_NULL',
        'SHT_PROGBITS',
        'SHT_SYMTAB',
        'SHT_STRTAB',
        'SHT_RELA',
        'SHT_HASH',
        'SHT_DYNAMIC',
        'SHT_NOTE',
        'SHT_NOBITS',
        'SHT_REL',
        'SHT_SHLIB',
        'SHT_DYNSYM',
    ]
    #SHT_LOPROC = 0x70000000
    #SHT_LOUSER = 0x80000000

    #def verify(self, val):
    #    if val & (self.SHT_LOPROC | self.SHT_LOUSER) == (self.SHT_LOPROC | self.SHT_LOUSER):
    #        return False
    #    if val & (self.SHT_LOPROC) not in (self.SHT_LOPROC, 0):
    #        return False

    #    return super().verify(val & ~(self.SHT_LOPROC | self.SHT_LOUSER))

    #def __repr__(self):
    #    data = self.data
    #    if data & self.SHT_LOUSER:
    #        return f'SHT'
