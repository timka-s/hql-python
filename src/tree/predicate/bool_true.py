from .__external__ import Predicate


class TRUE(Predicate):
    @classmethod
    def _make(cls):
        return cls._instance

    def __str__(self):
        return 'TRUE'


TRUE._instance = TRUE._create(tuple())
