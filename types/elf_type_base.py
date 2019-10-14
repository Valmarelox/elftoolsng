import struct


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
            print('Bad value in field {type}:{value}'.format(type=type(self), value=x))
        if len(x) == 1:
            x = x[0]
        return x

    def verify(self, *args):
        return True

    @data.setter
    def data(self, *args):
        if not self.verify(*args):
            assert False
        self.raw_write(struct.pack(self.STRUCT, *args))

    @classmethod
    def size(cls):
        return struct.calcsize(cls.STRUCT)