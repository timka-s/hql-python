from .__external__ import Expression


class Constant(Expression):
    __fields__ = ('data',)


    def __new__(cls, data):
        return cls._make(data)


    def __hash__(self):
        if self.data.__hash__:
            return hash(self.data)

        return id(self)


    def __str__(self):
        return '`%s`' % str(self.data)
