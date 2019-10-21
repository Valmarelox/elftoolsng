class ElfOffset(object):
    """
    Represents an offset that is dependant on the architecture on the ELF (ELFCLASS32/ELFCLASS64)
    """
    __slots__ = ('base', 'dynamic')

    def __init__(self, base=0, dynamic=0):
        if isinstance(base, ElfOffset):
            self.base = base.base
            self.dynamic = base.dynamic
        else:
            self.base = int(base)
            self.dynamic = int(dynamic)

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

    def __int__(self):
        if self.dynamic != 0:
            raise RuntimeError(f'Cannot convert dynamic offset to int, use {type(self).__name__}.{self.calc.__name__}')
