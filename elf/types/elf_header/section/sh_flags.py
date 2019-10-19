from elf.types.base.int.elf_int_bitmask import ElfIntNBitMask


class SHFlags(ElfIntNBitMask):
    BITS = [
        'SHF_WRITE',
        'SHF_ALLOC',
        'SHF_EXECINSTR',
        None,
        'SHF_MERGE',
    ]