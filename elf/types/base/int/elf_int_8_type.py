from elf.types.base.int.int_base_mixin import IntMixin
from elf.types.elf_type_base import ElfTypeBase


class ElfInt8Type(IntMixin, ElfTypeBase):
    STRUCT = 'B'
