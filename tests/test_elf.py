import pytest

from elf.elf import ELF
from elf.types.header.e_machine import EMachine


#def arm_binary():
#    return ELF(open(r'./binaries/a', 'rb').read())

def x86_64_binary():
    return ELF(open(r'../binaries/ls', 'rb').read())

def random_binary():
    return ELF(open(r'../test_elf.py', 'rb').read())


@pytest.mark.parametrize('binary', (x86_64_binary(),))
def test_elf_magic(binary):
    assert binary.header.e_ident.ei_magic.valid


def test_bad_elf():
    with pytest.raises(ValueError):
        e = x86_64_binary()


@pytest.mark.parametrize('binary,arch', ((x86_64_binary(), EMachine.EM_X86_64),))
def test_elf_machine(binary, arch):
    assert binary.header.e_machine == arch


@pytest.mark.parametrize('binary,arch', ((x86_64_binary(), EMachine.EM_X86_64),))
def test_edit_machine_arch(binary, arch):
    assert binary.header.e_machine == arch
    assert arch != EMachine.EM_MIPS
    binary.header.e_machine = EMachine.EM_MIPS
    assert binary.header.e_machine == EMachine.EM_MIPS
    binary.header.e_machine = arch
    assert binary.header.e_machine == arch
