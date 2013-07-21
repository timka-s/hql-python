from .__external__ import Source, Statement


class Input(Statement):
    __fields__ = ('source',)


    def __new__(cls, source):
        if not isinstance(source, Source):
            raise TypeError

        return cls._make(source)
