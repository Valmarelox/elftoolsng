from elf.types.section.header import SHType
from ..section_base import ElfSection


class DynamicSymbolSection(ElfSection):
    TYPE = SHType.SHT_DYNSYM