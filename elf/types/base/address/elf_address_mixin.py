
class ElfAddressMixin(object):
    def __repr__(self):
        return hex(self.data)