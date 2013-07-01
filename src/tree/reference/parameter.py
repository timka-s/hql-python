from .__external__ import Reference


class Parameter(Reference):
    def __str__(self):
        return '%%%s' % str(self.name)
