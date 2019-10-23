from elf.types.base.enum import ElfInt8Enum


class STOther(ElfInt8Enum):
    VALUES = (
        'STV_DEFAULT',
        'STV_INTERNAL',
        'STV_HIDDEN',
        'STV_PROTECTED',
    )