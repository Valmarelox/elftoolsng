from typing import Union

from elf.types.base import ElfOffset
from elf.types.base.int import ElfInt32Type


class ElfNameType(ElfInt32Type):

    @property
    def strtab_accessor(self) -> Union[int, bytes]:
        return b'.strtab'

    @property
    def strtab_exists(self) -> bool:
        if isinstance(self.strtab_accessor, bytes):
            return self.strtab_accessor in self.elf.sections
        elif isinstance(self.strtab_accessor, int):
            return 0 <= self.strtab_accessor < len(self.elf.sections)
        else:
            assert False

    @property
    def strtab(self):
        return self.elf.sections[self.strtab_accessor].section

    @property
    def string(self):
        if not self.strtab_exists:
            return b''
        return self.strtab.read_string(ElfOffset(self))

    def __repr__(self):
        return str(self)

    def __bytes__(self) -> bytes:
        return bytes(self.string)

    def __str__(self):
        return str(self.string)

    def __eq__(self, other):
        if isinstance(other, bytes):
            return bytes(self) == other
        elif isinstance(other, ElfNameType):
            return bytes(self) == bytes(other)
        else:
            return super().__eq__(other)

    def __lt__(self, other):
        if isinstance(other, bytes):
            return bytes(self) == other
        elif isinstance(other, ElfNameType):
            return bytes(self) < bytes(other)
        else:
            return super().__eq__(other)