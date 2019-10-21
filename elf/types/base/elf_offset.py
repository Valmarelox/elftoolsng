class ElfOffset(object):
    __slots__ = ('base', 'dynamic')

    def __init__(self, base=0, dynamic=0):
        if isinstance(base, ElfOffset):
            self.base = base.base
            self.dynamic = base.dynamic
        else:
            self.base = base
            self.dynamic = dynamic

    def calc(self, elf: 'ELF') -> int:
        return (8 if elf.is64bit else 4) * self.dynamic + self.base

    def __add__(self, other):
        if isinstance(other, int):
            return ElfOffset(self.base + other, self.dynamic)
        else:
            return ElfOffset(self.base + other.base, self.dynamic + other.dynamic)

    def __sub__(self, other):
        if isinstance(other, int):
            return ElfOffset(self.base - other, self.dynamic)
        else:
            return ElfOffset(self.base - other.base, self.dynamic - other.dynamic)

    def __repr__(self):
        return f'<ElfOffset base:{self.base} dynamic: {self.dynamic}>'
