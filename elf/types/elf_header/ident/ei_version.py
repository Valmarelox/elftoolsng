from elf.types.elf_header.base.int import ElfInt8Type


class EIVersion(ElfInt8Type):
    VALS = [
        'EV_NONE',
        'EV_CURRENT',
    ]
