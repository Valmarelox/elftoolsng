from elf.types.elf_header.ei_class import EIClass
from elf.types.elf_header.elf_header import ELFHeader


class ELF(object):
    def __init__(self, data):
        """
        :type data: bytes
        """
        super(ELF, self).__init__()
        self._data = bytearray(data)

    @property
    def is64bit(self):
        # TODO: Hack to prevent recursions
        return ord(self._data[4:5]) == EIClass.ELFCLASS64

    def sections(self):
        pass

    def raw_read(self, offset, size):
        return self._data[offset:offset + size]

    def raw_write(self, offset, data):
        """

        :type data: bytearray
        """
        self._data[offset:offset + len(data)] = data

    @property
    def header(self):
        return ELFHeader(self)

    @property
    def offset(self):
        return 0

    @property
    def elf(self):
        return self
