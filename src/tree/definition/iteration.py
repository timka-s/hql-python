from .__external__ import Expression, Definition, Alias


class Iteration(Definition):
    __fields__ = ('alias', 'expression')


    def __new__(cls, alias, expression):
        if not isinstance(alias, Alias):
            raise TypeError

        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(alias, expression)


    def __str__(self):
        return '%s IN %s' % (self.alias, self.expression)
