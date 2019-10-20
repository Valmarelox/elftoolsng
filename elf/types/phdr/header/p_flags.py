from elf.types.base.bitmask.elf_int_32_bitmask import ElfInt32BitMask


class PFlags(ElfInt32BitMask):
    BITS = [
        'PF_X',
        'PF_W',
        'PF_R'
    ]
