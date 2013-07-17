from .__external__ import Predicate, Iteration


class SequenceAccordance(Predicate):
    __fields__ = ('quantifier', 'iteration', 'predicate')
    __quantifiers__ = ('any', 'each')


    def __new__(cls, quantifier, iteration, predicate):
        if quantifier not in cls.__quantifiers__:
            raise ValueError

        if not isinstance(iteration, Iteration):
            raise TypeError

        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(quantifier, iteration, predicate)
