from elf.types.base.int import ElfInt16Enum


class EMachine(ElfInt16Enum):
    VALS = {
            0: 'EM_NONE',
            1: 'EM_M32',
            2: 'EM_SPARC',
            3: 'EM_386',
            4: 'EM_68K',
            5: 'EM_88K',
            7: 'EM_860',
            8: 'EM_MIPS',
            15: 'EM_PARISC',
            18: 'EM_SPARC32PLUS',
            20: 'EM_PPC',
            21: 'EM_PPC64',
            22: 'EM_S390',
            40: 'EM_ARM',
            42: 'EM_SH',
            43: 'EM_SPARCV9',
            50: 'EM_IA_64',
            62: 'EM_X86_64',
            75: 'EM_VAX'
    }
