from __future__ import annotations
from elf.types.section.header import SHType
from elf.types.section.types.section_base import ElfSection
from elf.types.section.types.strtab import StringTableSection


def construct_elf_section(header: 'ElfSectionHeader'):
    supported_types = {
        SHType.SHT_STRTAB: StringTableSection
    }
    if header.sh_type in supported_types:
        return supported_types[header.sh_type](header)
    else:
        return ElfSection(header)