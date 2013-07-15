from .__external__ import Expression


class Attribute(Expression):
    __fields__ = ('expression', 'name')


    def __new__(cls, expression, name):
        if not isinstance(expression, Expression):
            raise TypeError

        if not isinstance(name, str):
            raise TypeError

        return cls._make(expression, name)
