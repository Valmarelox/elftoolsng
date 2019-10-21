from elf.types.base import ElfOffset
from elf.types.base.str import ElfString
from elf.types.section.types import ProgBitsSection


class InterpreterSection(ProgBitsSection):
    NAME = b'.interp'

    @property
    def data(self) -> ElfString:
        return ElfString(self, ElfOffset(0))

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'<{type(self).__name__}: \'{str(self)}\'>'
