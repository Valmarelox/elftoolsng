from elf.types.section.header import SHType
from .section_base import ElfSection


class GnuHashSection(ElfSection):
    TYPE = SHType.SHT_GNU_HASH
