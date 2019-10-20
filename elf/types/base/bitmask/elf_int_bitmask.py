from elf.types.base.int.arch_int_meta_class import ArchIntMetaClass
from elf.types.base.elf_type_base import ElfTypeBase


class BitMaskMeta(type):
    BITS: ['str'] = []

    def __init__(mcs, name, bases, dct):
        for i, val in enumerate(mcs.BITS):
            if val is not None:
                setattr(mcs, val, i)
        super().__init__(name, bases, dct)


class IntNBitMaskMeta(ArchIntMetaClass, BitMaskMeta):
    pass


class BitMaskMixin(ElfTypeBase, metaclass=BitMaskMeta):
    BITS: ['str'] = []

    @classmethod
    def _get_full_mask(cls):
        mask = 0
        for index, bit in enumerate(cls.BITS):
            if bit is not None:
                mask |= (1 << index)

        return mask

    def __repr__(self):
        bits = []
        data = self.data
        for index, bit in enumerate(self.BITS):
            if data & (1 << index):
                bits.append(bit)
        return '|'.join(bits)

    def verify(self, val):
        return super().verify(val) and val & self._get_full_mask() == val


