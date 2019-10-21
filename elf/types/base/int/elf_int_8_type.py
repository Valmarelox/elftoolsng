from .int_base_mixin import IntMixin
from elf.types.base import ElfTypeBase


class ElfInt8Type(IntMixin, ElfTypeBase):
    STRUCT = 'B'
