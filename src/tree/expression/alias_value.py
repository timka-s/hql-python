from .__external__ import Expression, Alias


class AliasValue(Expression):
    __fields__ = ('alias',)


    def __new__(cls, alias):
        if not isinstance(alias, Alias):
            raise TypeError

        return cls._make(alias)
