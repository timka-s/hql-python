from .__external__ import Node


class Reference(Node):
    __fields__ = ('name', )


    def __new__(cls, name):
        if not isinstance(name, str):
            raise TypeError

        return cls._make(name)
