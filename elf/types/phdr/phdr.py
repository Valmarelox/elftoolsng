from elf.types.base.int import ElfInt32Type, ElfInt64Type
from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.base.struct.elf_meta import ElfMeta
from elf.types.phdr.header import PFlags, PType


class ElfProgramHeader32(ElfStruct):
    PROPERTIES = [
        ESP('p_type', PType),
        ESP('p_offset', ElfInt32Type),
        ESP('p_vaddr', ElfInt32Type),
        ESP('p_paddr', ElfInt32Type),
        ESP('p_filesz', ElfInt32Type),
        ESP('p_memsz', ElfInt32Type),
        ESP('p_flags', PFlags),
        ESP('p_align', ElfInt32Type)
    ]


class ElfProgramHeader64(ElfStruct):
    PROPERTIES = [
        ESP('p_type', PType),
        ESP('p_flags', PFlags),
        ESP('p_offset', ElfInt64Type),
        ESP('p_vaddr', ElfInt64Type),
        ESP('p_paddr', ElfInt64Type),
        ESP('p_filesz', ElfInt64Type),
        ESP('p_memsz', ElfInt64Type),
        ESP('p_align', ElfInt64Type)
    ]


class ElfProgramHeaderMeta(ElfMeta):
    def __call__(cls, *args, **kwargs):
        parent = args[0]
        if parent.elf.is64bit:
            return ElfProgramHeader64(*args, **kwargs)
        else:
            return ElfProgramHeader32(*args, **kwargs)


class ElfProgramHeader(ElfStruct, metaclass=ElfProgramHeaderMeta):
    pass
