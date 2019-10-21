from elf.types.section.header import SHType
from ..section_base import ElfSection


class SymbolTableSection(ElfSection):
    TYPE = SHType.SHT_SYMTAB