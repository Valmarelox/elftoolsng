from __future__ import annotations
import struct
from elf.types.base.elf_offset import ElfOffset


class ElfTypeBase(object):
    offset: ElfOffset
    elf: 'ELF'
    STRUCT = ''
    __slots__ = ('parent', 'elf', 'offset')

    def __init__(self, parent, offset):
        self.parent = parent
        self.elf = self.parent.elf
        self.offset = offset

    def raw_read(self, offset=ElfOffset(0), size=None) -> bytearray:
        if size is None:
            size = ElfOffset(len(self))
        return self.parent.raw_read(self.offset + offset, size=size)

    def raw_write(self, data, offset=0):
        assert data is bytearray or data is bytes
        self.parent.raw_write(data, self.offset + offset)

    @property
    def data(self):
        x = struct.unpack(self.STRUCT, self.raw_read())
        if not self.verify(*x):
            # print(f'Bad value in field {type(self)}:{x}')
            pass
        if len(x) == 1:
            x = x[0]
        return x

    def verify(self, *args) -> bool:
        return True

    def __eq__(self, other):
        if isinstance(other, ElfTypeBase):
            return self.data == other.data
        else:
            return self.data == other

    @property
    def valid(self) -> bool:
        return self.verify(self.data)

    @data.setter
    def data(self, *args):
        if not self.verify(*args):
            assert False
        self.raw_write(struct.pack(self.STRUCT, *args))

    @classmethod
    def size(cls) -> ElfOffset:
        return ElfOffset(struct.calcsize(cls.STRUCT))

    def __len__(self) -> int:
        return self.size().calc(self.elf)

    def __repr__(self):
        # return pformat({'Name': type(self).__name__, 'data': self.data})
        return str(self.data)

    def __hash__(self):
        return hash(self.data)
