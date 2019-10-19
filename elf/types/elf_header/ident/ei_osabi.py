from elf.types.elf_header.base.int import ElfInt8Enum


class EIOSAbi(ElfInt8Enum):
    VALS = ['ELFOSABI_NONE',
            'ELFOSABI_SYSV',
            'ELFOSABI_HPUX',
            'ELFOSABI_NETBSD',
            'ELFOSABI_LINUX',
            'ELFOSABI_SOLARIS',
            'ELFOSABI_IRIX',
            'ELFOSABI_FREEBSD',
            'ELFOSABI_TRU64',
            'ELFOSABI_ARM',
            'ELFOSABI_STANDALONE',
            ]
