from elf.types.elf_header.ident.ei_abiversion import EIAbiVersion
from elf.types.elf_header.ident.ei_osabi import EIOSAbi
from elf.types.elf_header.ident.ei_class import EIClass
from elf.types.elf_header.ident.ei_data import EIData
from elf.types.elf_header.ident.ei_magic import EIMagic
from elf.types.elf_header.ident.ei_pad import EIPad
from elf.types.elf_header.ident.ei_version import EIVersion
from elf.types.elf_header.base.struct.elf_struct import ElfStruct
from elf.types.elf_header.base.struct.elf_struct_property import ElfStructProperty as ESP


class EIdent(ElfStruct):
    PROPERTIES = [ESP('ei_magic', EIMagic),
                  ESP('ei_class', EIClass),
                  ESP('ei_data', EIData),
                  ESP('ei_version', EIVersion),
                  ESP('ei_osabi', EIOSAbi),
                  ESP('ei_abiversion', EIAbiVersion),
                  ESP('ei_pad', EIPad)]
