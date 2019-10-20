from elf.types.elf_header.ident.ei_class import EIClass
from elf.types.elf_header.elf_header import ELFHeader
from elf.types.elf_header.section.section_header import ElfSectionHeader
from elf.types.elf_offset import ElfOffset


class ElfSections(object):
    def __init__(self, elf):
        self.elf = elf

    def _get_section_by_index(self, index) -> ElfSectionHeader:
        offset = int(self.elf.header.e_shoff.data) + int(self.elf.header.e_shentsize.data) * int(index)
        print(f'Readin offset {offset}')
        return ElfSectionHeader(self.elf, offset)

    def __getitem__(self, item) -> ElfSectionHeader:
        if isinstance(item, str):
            for sec in self:
                if str(sec.sh_name) == item:
                    return sec
            else:
                raise KeyError()
        else:
            return self._get_section_by_index(item)

    def __getattr__(self, item):
        assert False

    def __iter__(self):
        count = self.elf.header.e_shnum
        for i in range(int(count)):
            yield self._get_section_by_index(i)


class ELF(object):
    def __init__(self, data):
        """
        :type data: bytes
        """
        super(ELF, self).__init__()
        self._data = bytearray(data)

    @property
    def is64bit(self):
        # TODO: Hack to prevent recursions
        return ord(self._data[4:5]) == EIClass.ELFCLASS64

    @property
    def sections(self):
        return ElfSections(self)

    def phdrs(self):
        pass

    def raw_read(self, offset, size):
        end_offset = offset + size
        return self._data[offset.calc(self):end_offset.calc(self)]

    def raw_write(self, offset, data):
        """
        :type data: bytearray
        """
        self._data[offset.calc(self):offset.calc(self) + len(data)] = data

    def raw_read_string(self, offset):
        read_end = self._data.find(b'\x00', offset.calc(self))
        return self.raw_read(offset, ElfOffset(read_end) - offset)

    @property
    def header(self):
        return ELFHeader(self, self.offset)

    @property
    def offset(self):
        return 0

    @property
    def elf(self):
        return self

    @property
    def data(self):
        return self._data
