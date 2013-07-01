from .__external__ import Expression, Definition, Alias


class AliasAssignment(Definition):
    __fields__ = ('expression', 'alias')


    def __new__(cls, expression, alias):
        if not isinstance(expression, Expression):
            raise TypeError

        if not isinstance(alias, Alias):
            raise TypeError

        return cls._make(expression, alias)


    def __str__(self):
        return '%s AS %s' % (self.expression, self.alias)
