from elf.types.base import ElfTypeBase
from elf.types.base.int import ElfInt32Type, ElfInt8Type, ElfInt16Type, ElfInt64Type
from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.base.struct.elf_meta import ElfMeta
from elf.types.symbol.st_info import STInfo
from elf.types.symbol.st_name import STName
from elf.types.symbol.st_other import STOther
from elf.types.symbol.st_shndx import STShndx


class ElfSymbolCommon(ElfTypeBase):
    def __repr__(self):
        return f"<ElfSymbol {self.parent.elf.sections[b'.strtab'].read_string(self.st_name)}>"


class ElfSymbol32(ElfStruct, ElfSymbolCommon):
    PROPERTIES = (
        ESP('st_name', STName),
        ESP('st_value', ElfInt32Type),
        ESP('st_size', ElfInt32Type),
        ESP('st_info', STInfo),
        ESP('st_other', STOther),
        ESP('st_shndx', STShndx)
    )


class ElfSymbol64(ElfStruct, ElfSymbolCommon):
    PROPERTIES = (
        ESP('st_name', STName),
        ESP('st_info', STInfo),
        ESP('st_other', STOther),
        ESP('st_shndx', STShndx),
        ESP('st_value', ElfInt64Type),
        ESP('st_size', ElfInt64Type),
    )


class ElfSymbolMeta(ElfMeta):
    def __call__(cls, *args, **kwargs):
        parent = args[0]
        if parent.elf.is64bit:
            return ElfSymbol64(*args, **kwargs)
        else:
            return ElfSymbol32(*args, **kwargs)


class ElfSymbol(ElfStruct, metaclass=ElfSymbolMeta):
    pass
