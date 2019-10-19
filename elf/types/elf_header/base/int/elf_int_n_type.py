from elf.types.elf_offset import ElfOffset
from elf.types.elf_header.base.int import ArchIntMetaClass


class ElfIntNType(metaclass=ArchIntMetaClass):
    STRUCT = 'X'

    @classmethod
    def size(cls):
        return ElfOffset(dynamic=1)