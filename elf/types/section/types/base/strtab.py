from typing import Iterator

from elf.types.base.elf_offset import ElfOffset
from elf.types.base.elf_type_base import ElfTypeBase
from elf.types.section.header import SHType
from elf.types.section.types.section_base import ElfSection


class ElfString(ElfTypeBase):
    STRUCT = ''
    parent: 'StringTableSection'

    def __init__(self, parent, offset):
        super().__init__(parent, offset)
        assert self.valid

    @classmethod
    def size(cls):
        raise NotImplementedError(f'{cls.__name__} Has no static length')

    def __len__(self) -> int:
        end = self.parent.data.find(b'\x00', self.offset.calc(self.elf))
        if end == -1:
            raise BufferError(f'No string found at offset {self.offset.calc(self.elf)}')
        return end - self.offset.calc(self.elf)

    @property
    def data(self):
        return bytes(self.raw_read())

    @data.setter
    def data(self, _data: bytes):
        self.raw_write(_data)

    def verify(self, data) -> bool:
        return isinstance(data, bytes)

    def __bytes__(self):
        return self.data

    def __str__(self):
        return str(bytes(self), 'ascii')

    def __lt__(self, other):
        return bytes(self) < bytes(other)

    def __eq__(self, other):
        return bytes(self) == bytes(other)
    #def __eq__(self, other):
    #return bytes(self) == other or bytes(self)[:len(self) - 1] == other


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
