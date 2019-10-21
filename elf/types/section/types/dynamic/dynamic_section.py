from elf.types.section.header import SHType
from elf.types.section.types.section_base import ElfSection


class DynamicSection(ElfSection):
    TYPE = SHType.SHT_DYNAMIC