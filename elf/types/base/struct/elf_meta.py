from elf.types.elf_offset import ElfOffset
from elf.types.base.int import ElfInt32Type
from elf.types.base.int import ElfInt64Type
from elf.types.base.int import ElfIntNType


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

        parent = args[0]
        curr_offset = ElfOffset(parent.offset)
        for index, prop in enumerate(cls.PROPERTIES):
            if prop.type == ElfIntNType:
                prop.type = ElfInt64Type if parent.elf.is64bit else ElfInt32Type
            getter = make_generic_getter(prop.type, curr_offset)
            setter = make_generic_setter(prop.type, curr_offset)
            setattr(cls, prop.name, property(getter,
                                             setter))
            curr_offset += prop.type.size()

        return super().__call__(*args, **kwargs)
