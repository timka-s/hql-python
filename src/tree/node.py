from .meta_node import MetaNode


class Node(tuple, metaclass=MetaNode):
    __fields__ = ()


    @classmethod
    def _make(cls, *args):
        return cls._create(args)


    @classmethod
    def _create(cls, args):
        return tuple.__new__(cls, args)


    def __new__(cls):
        return cls._make()


    def __init__(self, *args):
        pass


    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented

        return super().__eq__(other)


    def __ne__(self, other):
        if type(self) != type(other):
            return NotImplemented

        return super().__ne__(other)


    def __hash__(self):
        return super().__hash__()


    def __repr__(self):
        return '<%s.%s>\n    %s' % (
            type(self).__module__,
            type(self).__name__,
            '\n    '.join(
                ('%s:%s' % (name, repr(value))).replace('\n', '\n    ')
                for name, value in zip(self.__fields__, self)
            )
        )
