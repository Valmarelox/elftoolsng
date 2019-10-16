from elf.elf import ELF

f = ELF(open('./a.out', 'rb').read())
print(f.is64bit)