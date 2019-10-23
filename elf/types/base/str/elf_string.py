from elf.types.base import ElfTypeBase


class ElfString(ElfTypeBase):
    STRUCT = ''
    parent: 'StringTableSection'

    @classmethod
    def size(cls):
        raise NotImplementedError(f'{cls.__name__} Has no static length')

    def __len__(self) -> int:
        # Avoid using parent's data to avoid recursions
        end = self.parent.raw.find(b'\x00', self.offset.calc(self.elf))
        if end == -1:
            raise BufferError(f'No string found at offset {self.offset.calc(self.elf)}')
        return end - self.offset.calc(self.elf)

    @property
    def data(self):
        return bytes(self.raw)

    @data.setter
    def data(self, _data: bytes):
        self.raw = _data

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
