from elf.types.base.enum.elf_enum_base import EnumValsMeta, EnumMixin
from elf.types.base.int import ElfInt32Type


class ElfInt32Enum(EnumMixin, ElfInt32Type, metaclass=EnumValsMeta):
    pass