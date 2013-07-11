from .__external__ import NodeSet, Obtainment, KwargAssignment


class FunctionCall(Obtainment):
    __fields__ = ('name', 'kwarg_assignment_set')


    def __new__(cls, name, *kwarg_assignment_set):
        if not isinstance(name, str):
            raise TypeError

        kwarg_assignment_set = NodeSet(
            KwargAssignment, kwarg_assignment_set, False)

        kwarg_set = set(
            kwarg_assignment.kwarg for kwarg_assignment in kwarg_assignment_set)
        if len(kwarg_set) != len(kwarg_assignment_set):
            raise ValueError

        return cls._make(name, kwarg_assignment_set)
