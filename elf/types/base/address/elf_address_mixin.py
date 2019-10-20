from elf.types.base.elf_type_base import ElfTypeBase


class ElfAddressMixin(ElfTypeBase):
    def __repr__(self):
        return hex(self.data)
