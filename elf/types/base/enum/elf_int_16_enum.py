from elf.types.base.enum.elf_enum_base import EnumValuesMeta, EnumMixin
from elf.types.base.int import ElfInt16Type


class ElfInt16Enum(EnumMixin, ElfInt16Type, metaclass=EnumValuesMeta):
    pass
