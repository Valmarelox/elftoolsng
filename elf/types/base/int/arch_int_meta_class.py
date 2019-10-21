from . import ElfInt64Type
from . import ElfInt32Type


class ArchIntMetaClass(type):
    def __call__(cls, *args, **kwargs):
        parent = args[0]
        if parent.elf.is64bit:
            return ElfInt64Type(*args, **kwargs)
        else:
            return ElfInt32Type(*args, **kwargs)
