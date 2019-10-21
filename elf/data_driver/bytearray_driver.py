from elf.data_driver.base_driver import BaseDriver


class ByteArrayDriver(BaseDriver):
    __slots__ = ('_data',)
    _data: bytearray

    TYPES = [bytes, bytearray]

    def __init__(self, data: bytes):
        self._data = bytearray(data)

    def read(self, offset: int, size: int) -> bytearray:
        return self._data[offset: offset + size]

    def write(self, data: bytearray, offset: int):
        self._data[offset: offset + len(data)] = data

    @property
    def data(self) -> bytearray:
        return bytearray(self._data)