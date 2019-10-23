from elf.types.base.int import ElfInt16Type


class STShndx(ElfInt16Type):
    @property
    def section(self):
        return self.elf.sections[self.data]

    def __repr__(self):
        return f'<Section Index {self.data} points to {self.elf.sections[self.data].sh_name}>'
