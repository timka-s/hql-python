from .__external__ import Expression, Definition, Field


class FieldAssignment(Definition):
    __fields__ = ('field', 'expression')


    def __new__(cls, field, expression):
        if not isinstance(field, Field):
            raise TypeError

        if not isinstance(expression, Expression):
            raise TypeError

        return cls._make(field, expression)


    def __str__(self):
        return '%s = %s' % (self.field, self.expression)
