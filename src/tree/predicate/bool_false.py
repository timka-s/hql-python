from .__external__ import Predicate


class FALSE(Predicate):
    @classmethod
    def _make(cls):
        return cls._instance

    def __str__(self):
        return 'FALSE'


FALSE._instance = FALSE._create(tuple())
