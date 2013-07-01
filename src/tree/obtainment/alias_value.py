from .__external__ import Obtainment, Alias


class AliasValue(Obtainment):
    __fields__ = ('alias',)


    def __new__(cls, alias):
        if not isinstance(alias, Alias):
            raise TypeError

        return cls._make(alias)


    def __str__(self):
        return str(self.alias)
