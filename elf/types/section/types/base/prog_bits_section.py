from elf.types.section.header import SHType
from ..section_base import ElfSection


class ProgBitsSection(ElfSection):
    TYPE = SHType.SHT_PROGBITS