# Import all sections so they are registered by ElfSection.__subclasses()
# noinspection PyUnresolvedReferences
from elf.types.section.types import *
from elf.types.section.types.section_base import ElfSection


def construct_elf_section(header: 'ElfSectionHeader'):
    args = (header.parent, header)
    subclasses = tuple(filter(lambda sec: sec.TYPE == header.sh_type, ElfSection.__subclasses__()))
    # TODO: Acknowledge section name as well
    assert len(subclasses) == 1

    section_type = subclasses[0]
    if len(section_type.__subclasses__()) == 0:
        return section_type(*args)

    last = None
    for subclass in section_type.__subclasses__():
        if subclass.NAME is not None and subclass.NAME == bytes(header.sh_name):
            return subclass(*args)
        elif subclass.NAME is None: # Generic type
            last = subclass
    if last is not None:
        last(*args)
    else:
        return ElfSection(*args)
