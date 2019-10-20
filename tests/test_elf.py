import pytest

from elf.elf import ELF
from elf.types.header.e_machine import EMachine


def arm_binary():
    return ELF(open(r'./binaries/arm/strace-4.8', 'rb').read())


def random_binary():
    return ELF(open(r'./test_elf.py', 'rb').read())


@pytest.mark.parametrize('binary,valid', ((arm_binary(), True), (random_binary(), False)))
def test_elf_magic(binary, valid):
    assert binary.header.e_ident.ei_magic.valid == valid


@pytest.mark.parametrize('binary,arch', ((arm_binary(), EMachine.EM_ARM),))
def test_elf_machine(binary, arch):
    assert binary.header.e_machine == arch
