import pytest

from . import tree
from .visitor import Visitor


@pytest.fixture(scope='module')
def child_cls():
    class ChildVisitor(Visitor):
        def visit_Node(self, node):
            return True

    return ChildVisitor


def test_constructor_ok(child_cls):
    instance = child_cls(tree.Node._create(tuple()))
    assert isinstance(instance, child_cls)


def test_constructor_error_node():
    with pytest.raises(TypeError):
        Visitor(...)


def test_visit_error_not_implemented(child_cls):
    with pytest.raises(NotImplementedError):
        Visitor(tree.NodeSet._create(tuple()))
