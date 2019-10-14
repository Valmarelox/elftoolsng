from types.elf_header.ei_class import EIClass
from types.elf_header.ei_magic import EIMagic
from types.elf_struct import ElfStruct
from types.elf_struct_property import ElfStructProperty as ESP
from types.int.elf_int_n_type import ElfIntNType


class EIdent(ElfStruct):
    PROPERTIES = [ESP('ei_magic', EIMagic),
                  ESP('ei_class', EIClass),
                  ESP('ei_data', ElfIntNType),
                  ESP('ei_version', ElfIntNType),
                  ESP('ei_osabi', ElfIntNType)]