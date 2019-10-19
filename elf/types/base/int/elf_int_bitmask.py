from elf.types.base.int import ElfInt8Type, ElfInt16Type, ElfInt32Type, ElfInt64Type, ElfIntNType
from elf.types.base.int.arch_int_meta_class import ArchIntMetaClass
from elf.types.elf_type_base import ElfTypeBase


class BitMaskMeta(type):
    BITS: ['str'] = []

    def __init__(mcs, name, bases, dct):
        for i, val in enumerate(mcs.BITS):
            if val is not None:
                setattr(mcs, val, i)
        super().__init__(name, bases, dct)

    def __repr__(self):
        bits = []
        data = self.data
        for index, bit in enumerate(self.BITS):
            if data & (1 << index):
                bits.append(bit)
        return '|'.join(bits)


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

    def verify(self, val):
        return super().verify(val) and val & self._get_full_mask() == val


class ElfInt8BitMask(BitMaskMixin, ElfInt8Type, metaclass=BitMaskMeta):
    pass


class ElfInt16BitMask(BitMaskMixin, ElfInt16Type, metaclass=BitMaskMeta):
    pass


class ElfInt32BitMask(BitMaskMixin, ElfInt32Type, metaclass=BitMaskMeta):
    pass


class ElfInt64BitMask(BitMaskMixin, ElfInt64Type, metaclass=BitMaskMeta):
    pass


class ElfIntNBitMask(ElfIntNType, ElfInt64Type, metaclass=IntNBitMaskMeta):
    pass
