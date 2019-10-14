from types.int.elf_int_32_type import ElfInt32Type
from types.int.elf_int_64_type import ElfInt64Type
from types.int.elf_int_n_type import ElfIntNType


class ElfMeta(type):
    def __call__(cls, *args, **kwargs):
        def make_generic_getter(type, offset):
            def _generic_getter(self):
                return type(self, offset)

            return _generic_getter

        def make_generic_setter(type, offset):
            def _generic_setter(self, data):
                self.elf.raw_write(offset, data)

            return _generic_setter

        curr_offset = 0
        parent = args[0]
        for index, prop in enumerate(cls.PROPERTIES):
            if prop.type == ElfIntNType:
                prop.type = ElfInt64Type if parent.elf.is64bit else ElfInt32Type
            getter = make_generic_getter(prop.type, parent.offset + curr_offset)
            setter = make_generic_setter(prop.type, parent.offset + curr_offset)
            setattr(cls, prop.name, property(getter,
                                             setter))
            curr_offset += prop.type.size()

        obj = super().__call__(*args, **kwargs)
        return obj