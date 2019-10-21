from elf.types.base.enum import ElfInt32Enum


class SHType(ElfInt32Enum):
    VALUES = {
        0: 'SHT_NULL',
        1: 'SHT_PROGBITS',
        2: 'SHT_SYMTAB',
        3: 'SHT_STRTAB',
        4: 'SHT_RELA',
        5: 'SHT_HASH',
        6: 'SHT_DYNAMIC',
        7: 'SHT_NOTE',
        8: 'SHT_NOBITS',
        9: 'SHT_REL',
        10: 'SHT_SHLIB',
        11: 'SHT_DYNSYM',
        12: 'SHT_NUM',
        14: 'SHT_INIT_ARRAY',
        15: 'SHT_FINI_ARRAY',
        0x6ffffff6: 'SHT_GNU_HASH',
        0x6ffffffe: 'SHT_VERNEEED',
        0x6fffffff: 'SHT_VERSYM',
    }
    # SHT_LOPROC = 0x70000000
    # SHT_LOUSER = 0x80000000

    # def verify(self, val):
    #    if val & (self.SHT_LOPROC | self.SHT_LOUSER) == (self.SHT_LOPROC | self.SHT_LOUSER):
    #        return False
    #    if val & (self.SHT_LOPROC) not in (self.SHT_LOPROC, 0):
    #        return False

    #    return super().verify(val & ~(self.SHT_LOPROC | self.SHT_LOUSER))

    # def __repr__(self):
    #    data = self.data
    #    if data & self.SHT_LOUSER:
    #        return f'SHT'
