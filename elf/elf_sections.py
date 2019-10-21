from __future__ import annotations

from typing import Iterator

from elf.types.section import ElfSectionHeader


class ElfSections(object):
    elf: 'ELF'
    __slots__ = ('elf',)

    def __init__(self, elf):
        self.elf = elf

    def _get_section_by_index(self, index) -> ElfSectionHeader:
        if int(index) >= int(self.elf.header.e_shnum):
            raise KeyError(f'Index {int(index)} is bigger than section count: {int(self.elf.header.e_shnum)}')
        offset = int(self.elf.header.e_shoff.data) + int(self.elf.header.e_shentsize.data) * int(index)
        return ElfSectionHeader(self.elf, offset)

    def __getitem__(self, item) -> ElfSectionHeader:
        if isinstance(item, bytes):
            for sec in self:
                if bytes(sec.sh_name) == item:
                    return sec
            else:
                raise KeyError()
        else:
            return self._get_section_by_index(item)

    def __getattr__(self, item):
        assert False

    def __iter__(self) -> Iterator[ElfSectionHeader]:
        count = self.elf.header.e_shnum
        for i in range(int(count)):
            yield self._get_section_by_index(i)

    def __repr__(self):
        return f'<Section header table size={self.elf.header.e_shnum}>'
