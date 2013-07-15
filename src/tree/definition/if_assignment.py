from .__external__ import Expression, Definition, Predicate


class IfAssignment(Definition):
    __fields__ = ('predicate', 'expression')


    def __new__(cls, predicate, expression):
        if not isinstance(predicate, Predicate):
            raise TypeError

        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(predicate, expression)
