from elf.types.base.enum import ElfInt8Enum
from elf.types.base.int import ElfInt8Type


class STType(ElfInt8Enum):
    VALUES = (
        'STT_NOTYPE',
        'STT_OBJECT',
        'STT_FUNC',
        'STT_SECTION',
        'STT_FILE',
        'STT_COMMON',
        'STT_TLS',
    )

    @property
    def data(self):
        return super().data & 0xf

    @data.setter
    def data(self, val):
        assert self.verify(val)
        super().data = ((super().data & 0xf0) | (val & 0xf))


class STBind(ElfInt8Enum):
    VALUES = (
        'STB_LOCAL',
        'STB_GLOBAL',
        'STB_WEAK'
    )

    @property
    def data(self):
        return super().data >> 4

    @data.setter
    def data(self, val):
        assert self.verify(val)
        super().data = (val << 4) | (super().data & 0xf)


class STInfo(ElfInt8Type):

    @property
    def bind(self) -> STBind:
        return STBind(self, 0)

    @property
    def type(self) -> STType:
        return STType(self, 0)

    def __repr__(self):
        return '|'.join((repr(self.bind), repr(self.type)))
