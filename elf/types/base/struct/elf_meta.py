from elf.types.base.elf_offset import ElfOffset


class ElfMeta(type):
    def __call__(cls, *args, **kwargs):
        def make_generic_getter(t, offset):
            def _generic_getter(self):
                return t(self, offset)

            return _generic_getter

        def make_generic_setter(offset):
            def _generic_setter(self, data):
                self.elf.raw_write(offset, data)

            return _generic_setter

        start_offset = args[1]
        curr_offset = ElfOffset(start_offset)
        for index, prop in enumerate(cls.PROPERTIES):
            getter = make_generic_getter(prop.type, curr_offset)
            setter = make_generic_setter(curr_offset)
            setattr(cls, prop.name, property(getter,
                                             setter))
            curr_offset += prop.type.size()

        return super().__call__(*args, **kwargs)
