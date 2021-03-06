from .__external__ import NodeSet, Predicate


class Complex(Predicate):
    __fields__ = ('predicate_set',)


    @classmethod
    def _make(cls, predicate_set):
        def prepare():
            for predicate in predicate_set:
                if isinstance(predicate, cls):
                    for sub_predicate in predicate.predicate_set:
                        yield sub_predicate
                else:
                    yield predicate

        predicate_set = set(prepare())

        if len(predicate_set) == 1:
            return predicate_set.pop()
        else:
            return cls._create([NodeSet._make(predicate_set)])


    def __new__(cls, *predicate_set):
        return cls._make(NodeSet(Predicate, predicate_set))
