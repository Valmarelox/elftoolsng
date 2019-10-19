class ElfOffset(object):
    def __init__(self, base=0, dynamic=0):
        self.base = base
        self.dynamic = dynamic

    def calc(self, elf):
        return (8 if elf.is64bit else 4) * self.dynamic + self.base

    def __add__(self, other):
        if isinstance(other, int):
            return ElfOffset(self.base + other, self.dynamic)
        else:
            return ElfOffset(self.base + other.base, self.dynamic + other.dynamic)

    def __radd__(self, other):
        if isinstance(other, int):
            self.base += other
        else:
            self.base += other.base
            self.dynamic += other.dynamic

    def __repr__(self):
        return f'<ElfOffset base:{self.base} dynamic: {self.dynamic}>'
