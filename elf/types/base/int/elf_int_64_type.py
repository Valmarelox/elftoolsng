from .int_base_mixin import IntMixin
from elf.types.base import ElfTypeBase


class ElfInt64Type(IntMixin, ElfTypeBase):
    STRUCT = 'Q'
