from elf.types.base import ElfTypeBase


class EnumValuesMeta(type):
    VALUES: [int] = []

    def __init__(cls, name, bases, dct):
        if isinstance(cls.VALUES, dict):
            for (value, name) in cls.VALUES.items():
                setattr(cls, name, value)
        else:
            for i, val in enumerate(cls.VALUES):
                setattr(cls, val, i)

        super().__init__(name, bases, dct)


class EnumMixin(ElfTypeBase):
    VALUES = []

    def verify(self, val):
        if not super().verify(val):
            return False
        if isinstance(self.VALUES, dict):
            return val in self.VALUES
        else:
            return 0 <= val <= len(self.VALUES)

    def __repr__(self):
        try:
            return self.VALUES[self.data]
        except IndexError:
            raise KeyError(f'Value {self.data} not found in {type(self).__name__}')
        except KeyError:
            raise KeyError(f'Value {self.data} not found in {type(self).__name__}')
