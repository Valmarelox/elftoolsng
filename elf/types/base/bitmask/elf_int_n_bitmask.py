from elf.types.base.bitmask.elf_int_bitmask import IntNBitMaskMeta
from elf.types.base.int import ElfIntNType, ElfInt64Type


class ElfIntNBitMask(ElfIntNType, ElfInt64Type, metaclass=IntNBitMaskMeta):
    pass
