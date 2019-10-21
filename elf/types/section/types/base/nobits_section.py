from elf.types.section.header import SHType
from elf.types.section.types.section_base import ElfSection


class NoBitsSection(ElfSection):
    TYPE = SHType.SHT_NOBITS

    @property
    def data(self):
        return bytearray(len(self))

    @data.setter
    def data(self, other):
        raise NotImplementedError(f'Cannot set data for {type(self).__name__}')