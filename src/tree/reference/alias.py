from .__external__ import Reference


class Alias(Reference):
    def __str__(self):
        return '@%s' % str(self.name)
