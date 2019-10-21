from typing import Iterator

from elf.types.base.elf_offset import ElfOffset
from elf.types.section.types.section_base import ElfSection


class StringTableSection(ElfSection):

    def __iter__(self) -> Iterator[bytes]:
        offset = 0
        end = (self.offset + len(self)).calc(self.elf)
        while offset < end:
            try:
                s = self.read_string(offset)
            except BufferError as e:
                return
            yield s
            offset += (len(s) + 1)

    def read_string(self, start_offset: int) -> bytes:
        end_offset = self.data.find(b'\x00', start_offset, len(self))
        if end_offset == -1:
            raise BufferError(f'No string found at offset {start_offset}')
        return bytes(self.data[start_offset: end_offset])
