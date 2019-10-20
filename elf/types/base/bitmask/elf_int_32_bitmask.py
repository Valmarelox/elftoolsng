from elf.types.base.bitmask.elf_int_bitmask import BitMaskMixin, BitMaskMeta
from elf.types.base.int import ElfInt32Type


class ElfInt32BitMask(BitMaskMixin, ElfInt32Type, metaclass=BitMaskMeta):
    pass
