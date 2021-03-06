from __future__ import annotations
from elf.types.base import ElfOffset
from elf.types.base import ElfTypeBase


class ElfSection(ElfTypeBase):
    TYPE: int = None
    NAME: bytes = None

    def __init__(self, parent, header: 'ElfSectionHeader'):
        self.parent = parent
        self.elf = parent.elf
        self.header = header

    def size(self) -> ElfOffset:
        return ElfOffset(int(self.header.sh_size))

    def __len__(self):
        return int(self.header.sh_size)

    @property
    def offset(self) -> ElfOffset:
        return ElfOffset(int(self.header.sh_offset))

    @property
    def end_offset(self) -> ElfOffset:
        return self.offset + len(self)

    @property
    def name(self):
        return str(self.header.sh_name)

    @property
    def data(self) -> bytearray:
        return self.raw

    @data.setter
    def data(self, new_data: bytearray):
        self.raw = new_data

    def __repr__(self):
        return f'<{type(self).__name__} \'{self.name}\' size={len(self)}>'

    def __del__(self):
        # TODO: Delete section's data
        # TODO: Delete from section headers list
        # TODO: Fix all section offsets in section header list
        # TODO: Fix all sections indexi (symbol tables, e_shstrndx, dynamic symbol tables)
        raise NotImplementedError()
