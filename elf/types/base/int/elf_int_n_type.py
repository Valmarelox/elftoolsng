from elf.types.base.int.arch_int_meta_class import ArchIntMetaClass
from elf.types.base.elf_offset import ElfOffset


class ElfIntNType(metaclass=ArchIntMetaClass):
    STRUCT = 'X'

    @classmethod
    def size(cls):
        return ElfOffset(dynamic=1)
