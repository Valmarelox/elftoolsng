from __future__ import annotations
from elf.types.base.elf_offset import ElfOffset
from elf.types.base.elf_type_base import ElfTypeBase


class ElfSection(ElfTypeBase):
    def __init__(self, parent: 'ElfSectionHeader'):
        self.parent = parent
        self.elf = parent.elf

    def size(self) -> ElfOffset:
        return ElfOffset(int(self.parent.sh_size))

    @property
    def offset(self) -> ElfOffset:
        return ElfOffset(int(self.parent.sh_offset))

    @property
    def end_offset(self) -> ElfOffset:
        return self.offset + len(self)

    @property
    def name(self):
        return str(self.parent.sh_name)

    @property
    def data(self) -> bytearray:
        return self.raw_read()

    @data.setter
    def data(self, new_data: bytearray):
        self.raw_write(new_data)

    def __repr__(self):
        return f'<{type(self).__name__} \'{self.name}\' size={len(self)}>'
