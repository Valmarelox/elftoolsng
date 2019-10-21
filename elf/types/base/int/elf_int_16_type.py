from .int_base_mixin import IntMixin
from elf.types.base import ElfTypeBase


class ElfInt16Type(IntMixin, ElfTypeBase):
    STRUCT = 'H'
