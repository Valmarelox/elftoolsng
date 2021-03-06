from elf.types.base.enum.elf_enum_base import EnumValuesMeta, EnumMixin
from elf.types.base.int import ElfInt64Type


class ElfInt64Enum(EnumMixin, ElfInt64Type, metaclass=EnumValuesMeta):
    pass
