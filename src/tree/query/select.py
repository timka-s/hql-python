from .__external__ import Query, Declaration, Input


class Select(Query):
    __fields__ = ('declaration', 'input')


    def __new__(cls, declaration, input=None):
        if not isinstance(declaration, Declaration):
            raise TypeError

        if not isinstance(input, Input) and input is not None:
            raise TypeError

        return cls._make(declaration, input)
