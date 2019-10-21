from elf.types.base.bitmask import ElfIntNBitMask


class SHFlags(ElfIntNBitMask):
    BITS = (
        'SHF_WRITE',
        'SHF_ALLOC',
        'SHF_EXECINSTR',
        None,
        'SHF_MERGE',
    )
