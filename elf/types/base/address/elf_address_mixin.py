from elf.types.base import ElfTypeBase


class ElfAddressMixin(ElfTypeBase):
    def __repr__(self):
        return hex(self.data)
