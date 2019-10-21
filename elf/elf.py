from __future__ import annotations
from elf.elf_sections import ElfSections
from elf.types.base.elf_offset import ElfOffset
from elf.types.header.elf_header import ELFHeader
from elf.types.header.ident import EIClass
from elf.types.phdr.phdr import ElfProgramHeader


class ElfPhdrs(object):
    elf: ELF
    __slots__ = ('elf',)

    def __init__(self, elf):
        self.elf = elf

    def _get_section_by_index(self, index) -> ElfProgramHeader:
        if int(index) >= int(self.elf.header.e_phnum):
            raise KeyError(f'Index {int(index)} is bigger than section count: {int(self.elf.header.e_phnum)}')
        offset = int(self.elf.header.e_phoff.data) + int(self.elf.header.e_phentsize.data) * int(index)
        return ElfProgramHeader(self.elf, offset)

    def __getitem__(self, item) -> ElfProgramHeader:
        return self._get_section_by_index(item)

    def __repr__(self):
        return f'<Phdr table size={self.elf.header.e_phnum}>'


class ELF(object):
    _data: bytearray
    __slots__ = ('_data',)

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

    #def raw_read_string(self, offset):
    #    read_end = self._data.find(b'\x00', offset.calc(self))
    #    return self.raw_read(offset, ElfOffset(read_end) - offset)

    @property
    def header(self) -> ELFHeader:
        return ELFHeader(self, self.offset)

    @property
    def offset(self) -> ElfOffset:
        return ElfOffset(0)

    @property
    def elf(self) -> ELF:
        return self

    @property
    def data(self) -> bytearray:
        return self._data
