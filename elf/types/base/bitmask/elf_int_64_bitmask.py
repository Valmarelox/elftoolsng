from elf.types.base.bitmask.elf_int_bitmask import BitMaskMixin, BitMaskMeta
from elf.types.base.int import ElfInt64Type


class ElfInt64BitMask(BitMaskMixin, ElfInt64Type, metaclass=BitMaskMeta):
    pass
