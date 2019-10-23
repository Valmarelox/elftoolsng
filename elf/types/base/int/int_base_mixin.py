from elf.types.base import ElfTypeBase


class IntMixin(ElfTypeBase):
    def __int__(self):
        return int(self.data)

    def __iadd__(self, other):
        self.data += int(other)

    def __imul__(self, other):
        self.data *= int(other)

    def __idiv__(self, other):
        self.data /= int(other)
