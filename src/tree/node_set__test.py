import pytest

from .node import Node
from .node_set import NodeSet


@pytest.fixture(scope='module')
def instance(node_set):
    return node_set


def test_constructor_ok(instance):
    assert isinstance(instance, NodeSet)


def test_constructor_ok_node_set_empty():
    instance = NodeSet(Node, [], False)

    assert isinstance(instance, NodeSet)


def test_constructor_error_inner_cls(node):
    with pytest.raises(TypeError):
        NodeSet(str, [node])


def test_constructor_error_node_set_bad_type():
    with pytest.raises(TypeError):
        NodeSet(Node, ...)


def test_constructor_error_node_set_empty():
    with pytest.raises(ValueError):
        NodeSet(Node, [])


def test_constructor_error_node_set_bad_item_type(node):
    with pytest.raises(TypeError):
        NodeSet(Node, [node, ...])


def test_repr(instance):
    assert isinstance(repr(instance), str)


def test_str(instance):
    assert isinstance(str(instance), str)
