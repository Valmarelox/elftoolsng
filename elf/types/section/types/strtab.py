from typing import Iterator

from elf.types.base.elf_offset import ElfOffset
from elf.types.section.types.section_base import ElfSection


class StringTableSection(ElfSection):

    def __iter__(self) -> Iterator[bytes]:
        offset = ElfOffset(0)
        while offset < (self.offset + len(self)).calc(self.elf):
            try:
                s = self.read_string(offset)
            except BufferError as e:
                return
            yield s
            offset += (len(s) + 1)

    def read_string(self, start_offset: ElfOffset):
        offset = (self.offset + start_offset).calc(self.elf)
        end_offset = self.data.find(b'\x00', offset, self.end_offset.calc(self.elf))
        if end_offset == -1:
            raise BufferError(f'No string found at offset {offset}')
        return self.elf.raw_read(offset, end_offset - offset)
