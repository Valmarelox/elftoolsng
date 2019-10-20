from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.section.header import SHName, SHType, SHFlags, SHAddr, SHOffset, SHSize, SHLink, SHInfo, SHAddrAlign, \
    SHEntSize


class ElfSectionHeader(ElfStruct):
    PROPERTIES = [
        ESP('sh_name', SHName),
        ESP('sh_type', SHType),
        ESP('sh_flags', SHFlags),
        ESP('sh_addr', SHAddr),
        ESP('sh_offset', SHOffset),
        ESP('sh_size', SHSize),
        ESP('sh_link', SHLink),
        ESP('sh_info', SHInfo),
        ESP('sh_addralign', SHAddrAlign),
        ESP('sh_entsize', SHEntSize),
    ]
