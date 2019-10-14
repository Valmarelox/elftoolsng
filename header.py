import struct

from ElfStruct import ElfStruct, ElfStructProperty as ESP, ElfIntNType, ElfInt32Type, ElfInt16Type, \
    ElfInt8Type, ElfTypeBytes


class EIClass(ElfInt8Type):
    ELFCLASSNONE = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2

    @property
    def is64bit(self):
        return self.data == self.ELFCLASS64

    def verify(self, val):
        return val in [self.ELFCLASS32, self.ELFCLASS64]


class EIMagic(ElfTypeBytes(4)):
    def verify(self, val):
        return val == b'\x7fELF'


class EIdent(ElfStruct):
    PROPERTIES = [ESP('ei_magic', EIMagic),
                  ESP('ei_class', EIClass),
                  ESP('ei_data', ElfIntNType),
                  ESP('ei_version', ElfIntNType),
                  ESP('ei_osabi', ElfIntNType)]


class ELFHeader(ElfStruct):
    PROPERTIES = [ESP('e_ident', EIdent), ESP('e_type', ElfInt16Type), ESP('e_machine', ElfInt16Type),
                  ESP('e_version', ElfInt32Type)]

    def __init__(self, parent):
        super().__init__(parent, parent.offset)
