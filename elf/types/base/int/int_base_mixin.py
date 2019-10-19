
class IntMixin(object):
    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self.data + other.data)
        else:
            return type(self)(self.data + other)
