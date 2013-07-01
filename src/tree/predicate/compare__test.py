import pytest

from .compare import Compare


@pytest.fixture(scope='module')
def instance(compare):
    return compare


def test_constructor_ok(instance):
    assert isinstance(instance, Compare)


def test_constructor_error_comparision(expression):
    with pytest.raises(ValueError):
        Compare(..., expression, expression)


def test_constructor_error_left(expression):
    with pytest.raises(TypeError):
        Compare('!=', ..., expression)


def test_constructor_error_right(expression):
    with pytest.raises(TypeError):
        Compare('>=', expression, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
