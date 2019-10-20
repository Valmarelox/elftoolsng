from elf.types.elf_type_base import ElfTypeBase


class IntMixin(ElfTypeBase):
    def __int__(self):
        return int(self.data)
