from types.elf_type_bytes import ElfTypeBytes


class EIMagic(ElfTypeBytes(4)):
    def verify(self, val):
        return val == b'\x7fELF'