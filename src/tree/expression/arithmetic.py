from .__external__ import Expression


class Arithmetic(Expression):
    __fields__ = ('operator', 'left', 'right')
    __operators__ = ('+', '-', '*', '/')


    def __new__(cls, operator, left, right):
        if operator not in cls.__operators__:
            raise ValueError

        if not isinstance(left, Expression):
            raise TypeError

        if not isinstance(right, Expression):
            raise TypeError

        return cls._make(operator, left, right)
