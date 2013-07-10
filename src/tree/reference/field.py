from .__external__ import Reference


class Field(Reference):
    def __str__(self):
        return '%s' % str(self.name)
