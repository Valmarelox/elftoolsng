from io import BufferedReader, SEEK_SET

from elf.data_driver.base_driver import BaseDriver


class FileDriver(BaseDriver):
    __slots__ = ('f',)
    f: BufferedReader

    TYPES = [BufferedReader]

    def __init__(self, f):
        self.f = f

    def read(self, offset: int, size: int) -> bytearray:
        assert self.f.seek(offset, SEEK_SET) == offset
        return bytearray(self.f.read(size))

    def write(self, data: bytearray, offset: int):
        assert self.f.seek(offset, SEEK_SET) == offset
        self.f.write(data)
        self.f.flush()

    @property
    def data(self) -> bytearray:
        assert self.f.seek(0, SEEK_SET) == 0
        return bytearray(self.f.read())
