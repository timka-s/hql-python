from .__external__ import Predicate


class Not(Predicate):
    __fields__ = ('predicate',)


    @classmethod
    def _make(cls, predicate):
        if isinstance(predicate, cls):
            return predicate.predicate

        return cls._create([predicate])


    def __new__(cls, predicate):
        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(predicate)


    def __str__(self):
        return 'not %s' % str(self.predicate)
