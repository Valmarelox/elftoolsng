class EnumValsMeta(type):
    VALS: [int] = []

    def __init__(mcs, name, bases, dct):
        if isinstance(mcs.VALS, dict):
            for (value, name) in mcs.VALS.items():
                setattr(mcs, name, value)
        else:
            for i, val in enumerate(mcs.VALS):
                setattr(mcs, val, i)

        super().__init__(name, bases, dct)


class EnumMixin(object):
    VALS = []

    def verify(self, val):
        if not super().verify(val):
            return False
        if isinstance(self.VALS, dict):
            return val in self.VALS
        else:
            return 0 <= val <= len(self.VALS)

    def __repr__(self):
        try:
            return self.VALS[self.data]
        except KeyError:
            raise KeyError(f'Value {self.data} not found in {self.VALS}')