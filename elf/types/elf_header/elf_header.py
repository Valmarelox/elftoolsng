from elf.types.elf_header.e_machine import EMachine
from elf.types.elf_header.e_type import EType
from elf.types.elf_header.e_version import EVersion
from elf.types.base.int import ElfInt16Type
from elf.types.base.int import ElfInt32Type
from elf.types.base.int import ElfIntNType
from elf.types.base.struct import ElfStruct
from elf.types.base.struct import ElfStructProperty as ESP
from elf.types.elf_header.ident.e_ident import EIdent


class ELFHeader(ElfStruct):
    PROPERTIES = [ESP('e_ident', EIdent),
                  ESP('e_type', EType),
                  ESP('e_machine', EMachine),
                  ESP('e_version', EVersion),
                  ESP('e_entry', ElfIntNType),
                  ESP('e_phoff', ElfIntNType),
                  ESP('e_shoff', ElfIntNType),
                  ESP('e_flags', ElfInt32Type),
                  ESP('e_ehsize', ElfInt16Type),
                  ESP('e_phentsize', ElfInt16Type),
                  ESP('e_phnum', ElfInt16Type),
                  ESP('e_shentsize', ElfInt16Type),
                  ESP('e_shnum', ElfInt16Type),
                  ESP('e_shstrndx', ElfInt16Type)]
