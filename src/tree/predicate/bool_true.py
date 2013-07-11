from .__external__ import Predicate


class TRUE(Predicate):
    @classmethod
    def _make(cls):
        return cls._instance


TRUE._instance = TRUE._create(tuple())
