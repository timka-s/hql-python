from .__external__ import Obtainment, Predicate


class Verity(Obtainment):
    __fields__ = ('predicate',)


    def __new__(cls, predicate):
        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(predicate)
