from elf.types.elf_type_base import ElfTypeBase


def ElfTypeBytes(size):
    class ElfTypeBytes(ElfTypeBase):
        STRUCT = f'{size}s'

    return ElfTypeBytes
