from .__external__ import Source, Iteration


class Origin(Source):
    __fields__ = ('iteration',)


    def __new__(cls, iteration):
        if not isinstance(iteration, Iteration):
            raise TypeError

        return cls._make(iteration)
