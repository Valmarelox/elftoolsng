from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.header.ident import EIMagic, EIClass, EIData, EIVersion, EIOSAbi, EIAbiVersion, EIPad


class EIdent(ElfStruct):
    PROPERTIES = (
        ESP('ei_magic', EIMagic),
        ESP('ei_class', EIClass),
        ESP('ei_data', EIData),
        ESP('ei_version', EIVersion),
        ESP('ei_osabi', EIOSAbi),
        ESP('ei_abiversion', EIAbiVersion),
        ESP('ei_pad', EIPad)
    )
