
class IntMixin(object):
    def __int__(self):
        return int(self.data)
