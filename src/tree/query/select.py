from .__external__ import Query, Condition, Source, Declaration


class Select(Query):
    __fields__ = ('declaration', 'source', 'condition')


    def __new__(cls, declaration, source=None, condition=None):
        if not isinstance(declaration, Declaration):
            raise TypeError

        if not isinstance(source, Source) and source is not None:
            raise TypeError

        if not isinstance(condition, Condition) and condition is not None:
            raise TypeError

        return cls._make(declaration, source, condition)


    def __str__(self):
        def prepare():
            yield str(self.declaration)

            if self.source:
                yield str(self.source)

            if self.condition:
                yield str(self.condition)

        return ''.join(prepare())