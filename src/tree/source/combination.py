from .__external__ import NodeSet, Source


class Combination(Source):
    __fields__ = ('source_set',)


    def __new__(cls, *source_set):
        if len(source_set) < 2:
            raise ValueError

        return cls._make(NodeSet(Source, source_set))
