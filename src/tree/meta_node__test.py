import pytest

from .meta_node import MetaNode


@pytest.fixture(scope='module')
def base_fields():
    return ('a', 'b', 'c')


def test_constructor_ok_without_fields():
    class SomeNode(tuple, metaclass=MetaNode):
        pass

    assert isinstance(SomeNode, MetaNode)


def test_constructor_ok_with_fields(base_fields):
    class SomeNode(tuple, metaclass=MetaNode):
        __fields__ = base_fields

    assert isinstance(SomeNode, MetaNode)


def test_constructor_ok_without_new_fields(base_fields):
    class SomeNode(tuple, metaclass=MetaNode):
        __fields__ = base_fields

    class ChildNode(SomeNode):
        __fields__ = base_fields

    assert isinstance(ChildNode, MetaNode)


def test_constructor_error_multiply_bases():
    with pytest.raises(ValueError):
        class SomeNode(list, tuple, metaclass=MetaNode):
            pass


def test_constructor_error_base_not_tuple_subclass():
    with pytest.raises(TypeError):
        class SomeNode(list, metaclass=MetaNode):
            pass


def test_validate_fields_ok(base_fields):
    MetaNode._validate_fields(base_fields, base_fields) is None


def test_validate_fields_error_bad_type(base_fields):
    with pytest.raises(TypeError):
        MetaNode._validate_fields(base_fields, ...)


def test_validate_fields_error_less_fields(base_fields):
    with pytest.raises(ValueError):
        MetaNode._validate_fields(base_fields + ('h',), base_fields)


def test_validate_fields_error_bad_item_type(base_fields):
    with pytest.raises(TypeError):
        MetaNode._validate_fields(base_fields, base_fields + (...,))


def test_validate_fields_error_not_unique_fields(base_fields):
    with pytest.raises(ValueError):
        MetaNode._validate_fields(base_fields, base_fields + ('e', 'e'))


def test_get_attribute(base_fields):
    class SomeNode(tuple, metaclass=MetaNode):
        __fields__ = base_fields

    abc = [1, 2, 3]
    node = SomeNode(abc)

    assert [node.a, node.b, node.c] == abc
