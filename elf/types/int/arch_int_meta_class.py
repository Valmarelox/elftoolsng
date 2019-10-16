from elf.types.int.elf_int_64_type import ElfInt64Type
from elf.types.int.elf_int_32_type import ElfInt32Type


class ArchIntMetaClass(type):
    def __call__(cls, *args, **kwargs):
        parent = args[0]
        if parent.elf.is64bit:
            return ElfInt64Type(*args, **kwargs)
        else:
            return ElfInt32Type(*args, **kwargs)