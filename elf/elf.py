from __future__ import annotations

from elf.data_driver import build_driver, BaseDriver
from elf.elf_sections import ElfSections
from elf.types.base import ElfOffset
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
    _driver: BaseDriver

    def __init__(self, obj):
        super(ELF, self).__init__()
        self._driver = build_driver(obj)
        if not self.header.e_ident.ei_magic.valid:
            raise ValueError(f'data is not a valid ELF file!')

    @property
    def is64bit(self) -> bool:
        # TODO: Hack to prevent recursions
        return ord(self._driver.read(4, 1)) == EIClass.ELFCLASS64

    @property
    def sections(self) -> ElfSections:
        return ElfSections(self)

    @property
    def phdrs(self) -> ElfPhdrs:
        return ElfPhdrs(self)

    def raw_read(self, offset: ElfOffset, size: ElfOffset) -> bytearray:
        return self._driver.read(offset.calc(self), size.calc(self))

    def raw_write(self, data: bytearray, offset: ElfOffset):
        self._driver.write(data, offset.calc(self))

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
        return self._driver.data

    def __repr__(self):
        return f'<Elf arch={self.header.e_machine} endianess={self.header.e_ident.ei_data} wordsize=' \
               f'{self.header.e_ident.ei_data}>'