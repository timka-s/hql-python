from .__external__ import NodeSet, Statement, FieldAssignment


class Declaration(Statement):
    __fields__ = ('field_assignment_set',)


    def __new__(cls, *field_assignment_set):
        field_assignment_set = NodeSet(FieldAssignment, field_assignment_set)

        field_set = set(
            field_assignment.field for field_assignment in field_assignment_set)
        if len(field_set) != len(field_assignment_set):
            raise ValueError

        return cls._make(field_assignment_set)
