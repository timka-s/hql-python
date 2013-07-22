import pytest

from .arithmetic import Arithmetic


@pytest.fixture(scope='module')
def instance(arithmetic):
    return arithmetic


def test_constructor_ok(instance):
    assert isinstance(instance, Arithmetic)


def test_constructor_error_operator(expression):
    with pytest.raises(ValueError):
        Arithmetic(..., expression, expression)


def test_constructor_error_left(expression):
    with pytest.raises(TypeError):
        Arithmetic('+', ..., expression)


def test_constructor_error_right(expression):
    with pytest.raises(TypeError):
        Arithmetic('-', expression, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
