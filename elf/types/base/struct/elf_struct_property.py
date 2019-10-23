from elf.types.base import ElfTypeBase


class ElfStructProperty(object):
    def __init__(self, name: object, cls: object) -> object:
        super(ElfStructProperty, self).__init__()
        self.name = name
        self.type = cls
