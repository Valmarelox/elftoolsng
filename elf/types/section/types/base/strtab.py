from typing import Iterator

from elf.types.base import ElfOffset
from elf.types.base.str import ElfString
from elf.types.section.header import SHType
from ..section_base import ElfSection


class StringTableSection(ElfSection):
    TYPE = SHType.SHT_STRTAB

    def __iter__(self) -> Iterator[bytes]:
        offset = 0
        end = len(self)
        while offset < end:
            try:
                s = self.read_string(offset)
            except BufferError as e:
                return
            yield s
            offset += len(s) + 1

    def read_string(self, start_offset: int) -> ElfString:
        return ElfString(self, ElfOffset(start_offset))
