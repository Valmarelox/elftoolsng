from _io import BufferedReader

from header import ELFHeader


class ELF(object):
    def __init__(self, data):
        """
        :type data: bytes
        """
        super(ELF, self).__init__()
        self._data = data

    def sections(self):
        pass

    def raw_read(self, offset, size):
        return self._data[offset:offset+size]

    def raw_write(self, offset, data):
        """

        :type data: bytearray
        """
        self._data[offset:offset+len(data)] = data


    @property
    def header(self):
        return ELFHeader(self)
