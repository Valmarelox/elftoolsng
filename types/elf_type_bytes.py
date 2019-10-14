from types.elf_type_base import ElfTypeBase


def ElfTypeBytes(size):
    class ElfTypeBytes(ElfTypeBase):
        STRUCT = '{}s'.format(size)
    return ElfTypeBytes