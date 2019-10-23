from typing import Iterator

from elf.types.section.header import SHType
from elf.types.symbol.elf_symbol import ElfSymbol
from ..section_base import ElfSection


class SymbolTableSection(ElfSection):
    TYPE = SHType.SHT_SYMTAB

    def __iter__(self) -> Iterator[ElfSymbol]:
        offset = 0
        for index in range(self.count):
            yield self[index]

    @property
    def count(self):
        return int(self.header.sh_size) // int(self.header.sh_entsize)

    def __getitem__(self, item):
        # TODO: Verify offset
        if not (0 <= item < self.count):
            raise ValueError(f'Index {item} is out of range')
        offset = int(self.header.sh_entsize) * item
        return ElfSymbol(self, offset)

    def __repr__(self):
        return f'<SymbolTableSection \'{self.header.sh_name}\' symbol_count={self.count}>'