import pytest

from elf.elf import ELF


@pytest.fixture
def binary():
    return ELF(open(r'./binaries/arm/strace-4.8', 'rb').read())


def test_shstrtab(binary):
    assert binary.sections[binary.header.e_shstrndx].sh_name == b'.shstrtab'
    assert binary.sections[b'.shstrtab']