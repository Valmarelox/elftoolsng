from elf.types.base.bitmask import ElfInt32BitMask


class PFlags(ElfInt32BitMask):
    BITS = (
        'PF_X',
        'PF_W',
        'PF_R'
    )
