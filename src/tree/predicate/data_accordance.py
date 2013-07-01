from .__external__ import Predicate, AliasAssignment


class DataAccordance(Predicate):
    __fields__ = ('alias_assignment', 'predicate')


    def __new__(cls, alias_assignment, predicate):
        if not isinstance(alias_assignment, AliasAssignment):
            raise TypeError

        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(alias_assignment, predicate)


    def __str__(self):
        return '%s IS (%s)' % (self.alias_assignment, self.predicate)
