from .__external__ import Expression, Predicate


class CheckValue(Predicate):
    __fields__ = ('expression',)


    def __new__(cls, expression):
        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(expression)
