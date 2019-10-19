from elf.types.base.int import ElfInt8Enum


class EIData(ElfInt8Enum):
    VALS = [
        'ELFDATANONE',
        'ELFDATA2LSB',
        'ELFDATA2MSB'
    ]

