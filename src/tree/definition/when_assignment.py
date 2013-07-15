from .__external__ import Expression, Definition


class WhenAssignment(Definition):
    __fields__ = ('pattern', 'result')


    def __new__(cls, pattern, result):
        if not isinstance(pattern, Expression):
            raise TypeError

        if not isinstance(result, Expression):
            raise TypeError

        return cls._make(pattern, result)
