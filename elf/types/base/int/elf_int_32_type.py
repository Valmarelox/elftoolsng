from .int_base_mixin import IntMixin
from elf.types.base import ElfTypeBase


class ElfInt32Type(IntMixin, ElfTypeBase):
    STRUCT = 'I'
