from elf.types.base.enum.elf_enum_base import EnumValuesMeta, EnumMixin
from elf.types.base.int.elf_int_8_type import ElfInt8Type


class ElfInt8Enum(EnumMixin, ElfInt8Type, metaclass=EnumValuesMeta):
    pass
