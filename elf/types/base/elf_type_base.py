import struct

from elf.types.base.elf_offset import ElfOffset


class ElfTypeBase(object):
    STRUCT = ''

    def __init__(self, parent, offset):
        self.parent = parent
        self.elf = self.parent.elf
        self.offset = offset

    def raw_read(self):
        return self.elf.raw_read(self.offset, self.size())

    def raw_write(self, data):
        assert data is bytearray or data is bytes
        return self.elf.raw_write(self.offset, self.size())

    @property
    def data(self):
        x = struct.unpack(self.STRUCT, self.raw_read())
        if not self.verify(*x):
            # print(f'Bad value in field {type(self)}:{x}')
            pass
        if len(x) == 1:
            x = x[0]
        return x

    def verify(self, *args):
        return True

    def __eq__(self, other):
        if isinstance(other, ElfTypeBase):
            return self.data == other.data
        else:
            return self.data == other

    @property
    def valid(self):
        return self.verify(self.data)

    @data.setter
    def data(self, *args):
        if not self.verify(*args):
            assert False
        self.raw_write(struct.pack(self.STRUCT, *args))

    @classmethod
    def size(cls) -> ElfOffset:
        return ElfOffset(struct.calcsize(cls.STRUCT))

    def __repr__(self):
        # return pformat({'Name': type(self).__name__, 'data': self.data})
        return str(self.data)
