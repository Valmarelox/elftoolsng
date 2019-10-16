from elf.types.elf_header.ei_class import EIClass
from elf.types.elf_header.ei_magic import EIMagic
from elf.types.int.elf_int_n_type import ElfIntNType
from elf.types.struct.elf_struct import ElfStruct
from elf.types.struct.elf_struct_property import ElfStructProperty as ESP


class EIdent(ElfStruct):
    PROPERTIES = [ESP('ei_magic', EIMagic),
                  ESP('ei_class', EIClass),
                  ESP('ei_data', ElfIntNType),
                  ESP('ei_version', ElfIntNType),
                  ESP('ei_osabi', ElfIntNType)]
