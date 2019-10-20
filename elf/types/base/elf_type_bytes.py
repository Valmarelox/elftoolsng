from elf.types.base.elf_type_base import ElfTypeBase


def ElfTypeBytes(size):
    # noinspection PyShadowingNames
    class ElfTypeBytes(ElfTypeBase):
        STRUCT = f'{size}s'

    return ElfTypeBytes
