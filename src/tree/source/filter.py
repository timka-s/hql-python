from .__external__ import Predicate, Source


class Filter(Source):
    __fields__ = ('source', 'predicate')


    def __new__(cls, source, predicate):
        if not isinstance(source, Source):
            raise TypeError

        if not isinstance(predicate, Predicate):
            raise TypeError

        return cls._make(source, predicate)
