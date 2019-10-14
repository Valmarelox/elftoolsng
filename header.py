from ElfStruct import ElfStruct, ElfStructProperty


class ELFHeader(ElfStruct):
    FORMAT = '<16sHHIXXXIHHHHHH'
    PROPERTIES = ['e_ident', 'e_type', 'e_machine', 'e_version']

    def __init__(self, elf):
        super().__init__(elf)
