from .arch_int_meta_class import ArchIntMetaClass
from .int_base_mixin import IntMixin
from elf.types.base import ElfOffset


class ElfIntNType(IntMixin, metaclass=ArchIntMetaClass):
    STRUCT = 'X'

    @classmethod
    def size(cls):
        return ElfOffset(dynamic=1)
