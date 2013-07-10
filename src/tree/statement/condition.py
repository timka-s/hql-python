from .__external__ import Predicate, Statement


class Condition(Statement):
    __fields__ = ('predicate',)


    def __new__(cls, predicate):
        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(predicate)


    def __str__(self):
        return 'IF\n\t%s\n' % str(self.predicate).replace('\n', '\n\t')
