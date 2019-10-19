from elf.types.base.int import ElfInt16Enum


class EType(ElfInt16Enum):
    VALS = [
        'ET_NONE',
        'ET_REL',
        'ET_EXEC',
        'ET_DYN',
        'ET_CORE'
    ]
