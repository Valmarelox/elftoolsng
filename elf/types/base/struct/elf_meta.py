from elf.types.base import ElfOffset


class ElfMeta(type):
    def __new__(cls, name, bases, dctn):
        if 'PROPERTIES' in dctn:
            dctn['__slots__'] = tuple(map(lambda prop: prop.name, dctn['PROPERTIES']))
        return super().__new__(cls, name, bases, dctn)

    def __init__(cls, *args, **kwargs):
        def make_generic_getter(t, offset):
            def _generic_getter(self):
                return t(self, offset)

            return _generic_getter

        def make_generic_setter(t, offset):
            def _generic_setter(self, data):
                t(self, offset).data = data

            return _generic_setter

        curr_offset = ElfOffset(0)
        for index, prop in enumerate(cls.PROPERTIES):
            getter = make_generic_getter(prop.type, curr_offset)
            setter = make_generic_setter(prop.type, curr_offset)
            setattr(cls, prop.name, property(getter,
                                             setter))
            curr_offset += prop.type.size()

        super().__init__(*args, **kwargs)
