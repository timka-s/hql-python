from collections import Iterable

from .node import Node


class NodeSet(Node):
    @classmethod
    def _make(cls, node_set):
        return cls._create(node_set)


    def __new__(cls, inner_cls, node_set):
        if not issubclass(inner_cls, Node):
            raise TypeError

        if not isinstance(node_set, Iterable):
            raise TypeError

        if not node_set:
            raise ValueError

        if not all(isinstance(node, inner_cls) for node in node_set):
            raise TypeError

        return cls._make(node_set)


    def __repr__(self):
        return '\n    ' + '\n    '.join(
            repr(node).replace('\n', '\n    ')
            for node in self
        )
