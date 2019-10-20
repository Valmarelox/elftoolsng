from elf.types.base.enum.elf_int_n_enum import ElfIntNEnum


class PType(ElfIntNEnum):
    VALS = {
        0: 'PT_NULL',
        1: 'PT_LOAD',
        2: 'PT_DYNAMIC',
        3: 'PT_INTERP',
        4: 'PT_NOTE',
        5: 'PT_SHLIB',
        6: 'PT_PHDR',
        7: 'PT_TLS',
        0x6474e550: 'PT_GNU_EH_FRAME',
        0x6474e551: 'PT_GNU_STACK',
    }