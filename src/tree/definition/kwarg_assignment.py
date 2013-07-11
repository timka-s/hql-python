from .__external__ import Expression, Definition, Kwarg


class KwargAssignment(Definition):
    __fields__ = ('kwarg', 'expression')


    def __new__(cls, kwarg, expression):
        if not isinstance(kwarg, Kwarg):
            raise TypeError

        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(kwarg, expression)
