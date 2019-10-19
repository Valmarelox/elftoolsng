from elf.types.base.int import ElfInt32Type, ElfIntNType
from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.elf_header.section.sh_flags import SHFlags
from elf.types.elf_header.section.sh_name import SHName
from elf.types.elf_header.section.sh_type import SHType


class ElfSectionHeader(ElfStruct):
    PROPERTIES = [
        ESP('sh_name', SHName),
        ESP('sh_type', SHType),
        ESP('sh_flags', SHFlags),
        ESP('sh_addr', ElfIntNType),
        ESP('sh_offset', ElfIntNType),
        ESP('sh_size', ElfIntNType),
        ESP('sh_link', ElfInt32Type),
        ESP('sh_info', ElfInt32Type),
        ESP('sh_addralign', ElfIntNType),
        ESP('sh_entsize', ElfIntNType),
    ]
