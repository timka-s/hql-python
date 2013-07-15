from .__external__ import NodeSet, Expression, Obtainment, IfAssignment


class IfValue(Obtainment):
    __fields__ = ('default', 'if_assignment_set')


    def __new__(cls, default, *if_assignment_set):
        if not isinstance(default, Expression):
            raise TypeError

        if_assignment_set = NodeSet(IfAssignment, if_assignment_set)

        return cls._make(default, if_assignment_set)
