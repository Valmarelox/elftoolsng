
class BaseDriver(object):
    def read(self, offset: int, size: int) -> bytearray:
        raise NotImplementedError()

    def write(self, data: bytes, offset: int):
        raise NotImplementedError()

    @property
    def data(self) -> bytearray:
        raise NotImplementedError()
