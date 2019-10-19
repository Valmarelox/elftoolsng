from elf.types.elf_type_bytes import ElfTypeBytes


class EIMagic(ElfTypeBytes(4)):
    MAGIC = b'\x7fELF'

    def verify(self, val):
        return val == self.MAGIC
