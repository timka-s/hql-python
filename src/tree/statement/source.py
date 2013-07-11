from .__external__ import NodeSet, Statement, Iteration


class Source(Statement):
    __fields__ = ('iteration_set',)


    def __new__(cls, *iteration_set):
        iteration_set = NodeSet(Iteration, iteration_set)

        alias_set = set(iteration.alias for iteration in iteration_set)
        if len(alias_set) != len(iteration_set):
            raise ValueError

        return cls._make(iteration_set)
