from elf.types.base.bitmask.elf_int_bitmask import BitMaskMixin, BitMaskMeta
from elf.types.base.int import ElfInt8Type


class ElfInt8BitMask(BitMaskMixin, ElfInt8Type, metaclass=BitMaskMeta):
    pass