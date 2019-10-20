from elf.types.base.enum import ElfInt16Enum


class EType(ElfInt16Enum):
    VALUES = [
        'ET_NONE',
        'ET_REL',
        'ET_EXEC',
        'ET_DYN',
        'ET_CORE'
    ]
