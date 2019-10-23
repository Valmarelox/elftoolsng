from elf.types.base import ElfTypeBase


class IntMixin(ElfTypeBase):
    def __int__(self):
        return int(self.data)