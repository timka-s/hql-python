from .__external__ import NodeSet, Expression, Obtainment, WhenAssignment


class CaseValue(Obtainment):
    __fields__ = ('expression', 'default', 'when_assignment_set')


    def __new__(cls, expression, default, *when_assignment_set):
        if not isinstance(expression, Expression):
            raise TypeError

        if not isinstance(default, Expression):
            raise TypeError

        when_assignment_set = NodeSet(WhenAssignment, when_assignment_set)

        return cls._make(expression, default, when_assignment_set)
