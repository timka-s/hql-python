from .__external__ import Expression, Definition, Alias


class Iteration(Definition):
    __fields__ = ('alias', 'expression')


    def __new__(cls, alias, expression):
        if not isinstance(alias, Alias):
            raise TypeError

        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(alias, expression)
