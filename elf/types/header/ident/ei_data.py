from elf.types.base.enum import ElfInt8Enum


class EIData(ElfInt8Enum):
    VALUES = [
        'ELFDATANONE',
        'ELFDATA2LSB',
        'ELFDATA2MSB'
    ]

