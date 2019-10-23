from __future__ import annotations

from elf.data_driver import build_driver, BaseDriver
from elf.elf_phrs import ElfPhdrs
from elf.elf_sections import ElfSections
from elf.types.base import ElfOffset
from elf.types.header.elf_header import ELFHeader
from elf.types.header.ident import EIClass


class ELF(object):
    _driver: BaseDriver
    __slots__ = ('_driver',)

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
        """
        Elf's Sections
        """
        return ElfSections(self)

    @property
    def phdrs(self) -> ElfPhdrs:
        """
        Elf's Program Headers
        """
        return ElfPhdrs(self)

    def raw_read(self, offset: ElfOffset, size: ElfOffset) -> bytearray:
        return self._driver.read(offset.calc(self), size.calc(self))

    def raw_write(self, data: bytearray, offset: ElfOffset):
        self._driver.write(data, offset.calc(self))

    @property
    def header(self) -> ELFHeader:
        """
        Elf's Header (struct EHdr)
        """
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