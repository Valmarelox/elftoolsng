from elf.types.base.bitmask.elf_int_n_bitmask import ElfIntNBitMask


class SHFlags(ElfIntNBitMask):
    BITS = [
        'SHF_WRITE',
        'SHF_ALLOC',
        'SHF_EXECINSTR',
        None,
        'SHF_MERGE',
    ]
