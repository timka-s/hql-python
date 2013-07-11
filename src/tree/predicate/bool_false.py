from .__external__ import Predicate


class FALSE(Predicate):
    @classmethod
    def _make(cls):
        return cls._instance


FALSE._instance = FALSE._create(tuple())
