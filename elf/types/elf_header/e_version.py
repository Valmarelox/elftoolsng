from elf.types.elf_header.base.int import ElfInt32Enum


class EVersion(ElfInt32Enum):
    VALS = [
        'EV_NONE',
        'EV_CURRENT'
    ]
