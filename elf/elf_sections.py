from __future__ import annotations

from typing import Iterator

from elf.types.base import ElfOffset
from elf.types.section import ElfSectionHeader


class ElfSections(object):
    elf: 'ELF'
    __slots__ = ('elf',)

    def __init__(self, elf):
        self.elf = elf

    def _get_section_by_index(self, index) -> ElfSectionHeader:
        if int(index) >= len(self):
            raise KeyError(f'Index {int(index)} is out of section table (size={int(self.elf.header.e_shnum)})')
        offset = int(self.elf.header.e_shoff.data) + int(self.elf.header.e_shentsize.data) * int(index)
        return ElfSectionHeader(self.elf, ElfOffset(offset))

    def __getitem__(self, item) -> ElfSectionHeader:
        if isinstance(item, bytes):
            for sec in self:
                if bytes(sec.sh_name) == item:
                    return sec
            else:
                raise KeyError(f'{item} not found in section table')
        else:
            try:
                return self._get_section_by_index(item)
            except ValueError:
                raise KeyError(f'{item} is of a wrong type ({type(item).__name__}')

    def __iter__(self) -> Iterator[ElfSectionHeader]:
        count = self.elf.header.e_shnum
        for i in range(int(count)):
            yield self._get_section_by_index(i)

    def __repr__(self):
        return f'<Section header table size={self.elf.header.e_shnum}>'

    def __contains__(self, item):
        assert isinstance(item, bytes)
        return item in map(lambda section: section.sh_name, self)

    def __len__(self):
        return int(self.elf.header.e_shnum)