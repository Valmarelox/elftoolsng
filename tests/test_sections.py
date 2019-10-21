import pytest

from elf.elf import ELF
from elf.types.section.types import NoBitsSection
from elf.types.section.types.dynamic import InterpreterSection


@pytest.fixture
def binary():
    return ELF(open(r'./binaries/arm/strace-4.8', 'rb').read())


@pytest.fixture
def dynamic_binary():
    return ELF(open(r'./binaries/bash', 'rb').read())


def test_shstrtab(binary):
    assert binary.sections[binary.header.e_shstrndx].sh_name == b'.shstrtab'
    assert binary.sections[b'.shstrtab']


def test_bss(binary):
    assert type(binary.sections[b'.bss'].section) == NoBitsSection
    assert binary.sections[b'.bss'].section.data == bytearray(len(binary.sections[b'.bss'].section.data))
    with pytest.raises(NotImplementedError):
        binary.sections[b'.bss'].section.data = bytearray(100)


def test_section_strtab_iter(binary):
    names = sorted(binary.sections[binary.header.e_shstrndx].section)
    sections = sorted(binary.sections)
    for (name, sec) in zip(names, sections):
        assert str(name) == str(sec.sh_name)


def test_none_existing_section(binary):
    with pytest.raises(KeyError):
        a = binary.sections[b'.gasgasgasgasgasga']
    with pytest.raises(KeyError):
        a = binary.sections['sgagasgasg']


def test_named_section_builder(dynamic_binary):
    assert type(dynamic_binary.sections[b'.interp'].section) == InterpreterSection
