from elf.types.phdr.phdr import ElfProgramHeader


class ElfPhdrs(object):
    elf: 'ELF'
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