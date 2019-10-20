from elf.types.base.bitmask.elf_int_bitmask import BitMaskMixin, BitMaskMeta
from elf.types.base.int import ElfInt16Type


class ElfInt16BitMask(BitMaskMixin, ElfInt16Type, metaclass=BitMaskMeta):
    pass
