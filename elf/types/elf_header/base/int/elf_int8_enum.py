from elf.types.elf_header.base.int.elf_int_16_type import ElfInt16Type
from elf.types.elf_header.base.int import ElfInt32Type
from elf.types.elf_header.base.int import ElfInt64Type
from elf.types.elf_header.base.int import ElfInt8Type


class EnumValsMeta(type):
    VALS: [int] = []

    def __init__(mcs, name, bases, dct):
        if isinstance(mcs.VALS, dict):
            for (value, name) in mcs.VALS.items():
                setattr(mcs, name, value)
        else:
            for i, val in enumerate(mcs.VALS):
                setattr(mcs, val, i)

        super().__init__(name, bases, dct)


class EnumMixin(object):
    VALS = []

    def verify(self, val):
        if not super().verify(val):
            return False
        if isinstance(self.VALS, dict):
            return val in self.VALS
        else:
            return 0 <= val <= len(self.VALS)

    def __repr__(self):
        return self.VALS[self.data]


class ElfInt8Enum(EnumMixin, ElfInt8Type, metaclass=EnumValsMeta):
    pass


class ElfInt16Enum(EnumMixin, ElfInt16Type, metaclass=EnumValsMeta):
    pass


class ElfInt32Enum(EnumMixin, ElfInt32Type, metaclass=EnumValsMeta):
    pass


class ElfInt64Enum(EnumMixin, ElfInt64Type, metaclass=EnumValsMeta):
    pass
