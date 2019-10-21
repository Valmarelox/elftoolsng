from elf.types.section.types.section_base import ElfSection
# Import all sections so they are registered by ElfSection.__subclasses()
# noinspection PyUnresolvedReferences
from . import *


def construct_elf_section(header: 'ElfSectionHeader'):
    l = tuple(filter(lambda sec: sec.TYPE == header.sh_type, ElfSection.__subclasses__()))
    # TODO: Acknowledge section name as well
    assert len(l) <= 1
    if l:
        subclass = l[0]
        return subclass(header.parent, header)
    else:
        return ElfSection(header.parent, header)
