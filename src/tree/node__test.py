import pytest

from .node import Node


@pytest.fixture(scope='module')
def instance(node):
    return node


@pytest.fixture(scope='module')
def some_node_cls():
    class SomeNode(Node):
        __fields__ = ('field',)

    return SomeNode


@pytest.fixture(scope='module')
def some_instance_a(some_node_cls):
    return some_node_cls._create(['a_field'])


@pytest.fixture(scope='module')
def some_instance_b(some_node_cls):
    return some_node_cls._create(['b_field'])


def test_constructor():
    assert isinstance(Node(), Node)


def test_eq_true(instance):
    assert instance == instance


def test_eq_false_different_types(instance, some_instance_a):
    assert not(instance == some_instance_a)


def test_eq_false_different_content(some_instance_a, some_instance_b):
    assert not(some_instance_a == some_instance_b)


def test_ne_false_with_self(instance):
    assert not(instance != instance)


def test_ne_true_different_types(instance, some_instance_a):
    assert instance != some_instance_a


def test_ne_true_different_content(some_instance_a, some_instance_b):
    assert some_instance_a != some_instance_b


def test_hash(instance):
    assert hash(instance)


def test_repr(instance):
    assert isinstance(repr(instance), str)
