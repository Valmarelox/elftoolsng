from .bytearray_driver import ByteArrayDriver
from .file_driver import FileDriver
from .base_driver import BaseDriver


def build_driver(data_source) -> BaseDriver:
    if type(data_source) in ByteArrayDriver.TYPES:
        return ByteArrayDriver(data_source)
    elif type(data_source) in FileDriver.TYPES:
        return FileDriver(data_source)
    else:
        raise NotImplementedError(f'No driver found for {type(data_source).__name__}')
