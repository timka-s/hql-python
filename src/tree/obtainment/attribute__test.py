import pytest

from .attribute import Attribute


@pytest.fixture(scope='module')
def instance(attribute):
    return attribute


def test_constructor_ok(instance):
    assert isinstance(instance, Attribute)


def test_constructor_error_expression():
    with pytest.raises(TypeError):
        Attribute(..., 'attribute_name')


def test_constructor_error_name(expression):
    with pytest.raises(TypeError):
        Attribute(expression, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
