from .__external__ import Expression, Obtainment


class Attribute(Obtainment):
    __fields__ = ('expression', 'name')


    def __new__(cls, expression, name):
        if not isinstance(expression, Expression):
            raise TypeError

        if not isinstance(name, str):
            raise TypeError

        return cls._make(expression, name)


    def __str__(self):
        return '%s.%s' % (self.expression, self.name)
