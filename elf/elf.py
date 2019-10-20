from elf.elf_phdrs import ElfPhdrs
from elf.elf_sections import ElfSections
from elf.types.base.elf_offset import ElfOffset
from elf.types.header.elf_header import ELFHeader
from elf.types.header.ident import EIClass


class ELF(object):
    def __init__(self, data: bytes):
        super(ELF, self).__init__()
        self._data = bytearray(data)

    @property
    def is64bit(self) -> bool:
        # TODO: Hack to prevent recursions
        return ord(self._data[4:5]) == EIClass.ELFCLASS64

    @property
    def sections(self) -> ElfSections:
        return ElfSections(self)

    @property
    def phdrs(self) -> ElfPhdrs:
        return ElfPhdrs(self)

    def raw_read(self, offset: ElfOffset, size: ElfOffset) -> bytearray:
        end_offset = offset + size
        return self._data[offset.calc(self): end_offset.calc(self)]

    def raw_write(self, offset: ElfOffset, data: bytearray):
        self._data[offset.calc(self): offset.calc(self) + len(data)] = data

    def raw_read_string(self, offset):
        read_end = self._data.find(b'\x00', offset.calc(self))
        return self.raw_read(offset, ElfOffset(read_end) - offset)

    @property
    def header(self) -> ELFHeader:
        return ELFHeader(self, self.offset)

    @property
    def offset(self) -> ElfOffset:
        return ElfOffset(0)

    @property
    def elf(self):
        return self

    @property
    def data(self) -> bytearray:
        return self._data
