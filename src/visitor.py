from . import tree


class Visitor():
    def __init__(self, node):
        if not isinstance(node, tree.Node):
            raise TypeError

        self.output = self.visit(node)


    def visit(self, node):
        method_name = 'visit_%s' % node.__class__.__name__

        if not hasattr(self, method_name):
            raise NotImplementedError

        return getattr(self, method_name)(node)
