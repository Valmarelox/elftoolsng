from types.elf_header.e_ident import EIdent
from types.struct.elf_struct import ElfStruct
from types.struct.elf_struct_property import ElfStructProperty as ESP
from types.int.elf_int_16_type import ElfInt16Type
from types.int.elf_int_32_type import ElfInt32Type


class ELFHeader(ElfStruct):
    PROPERTIES = [ESP('e_ident', EIdent), ESP('e_type', ElfInt16Type), ESP('e_machine', ElfInt16Type),
                  ESP('e_version', ElfInt32Type)]

    def __init__(self, parent):
        super().__init__(parent, parent.offset)