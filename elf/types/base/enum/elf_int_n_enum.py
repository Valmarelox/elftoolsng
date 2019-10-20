from elf.types.base.enum.elf_enum_base import EnumValsMeta, EnumMixin
from elf.types.base.int import ElfIntNType
from elf.types.base.int.arch_int_meta_class import ArchIntMetaClass


class ElfIntNEnumMeta(EnumValsMeta, ArchIntMetaClass):
    pass


class ElfIntNEnum(EnumMixin, ElfIntNType, metaclass=ElfIntNEnumMeta):
    pass
