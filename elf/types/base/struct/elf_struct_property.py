class ElfStructProperty(object):
    def __init__(self, name: str, cls: type):
        super(ElfStructProperty, self).__init__()
        self.name = name
        self.type = cls
