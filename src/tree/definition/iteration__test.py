import pytest

from .iteration import Iteration


@pytest.fixture(scope='module')
def instance(iteration):
    return iteration


def test_constructor_ok(instance):
    assert isinstance(instance, Iteration)


def test_constructor_error_alias(expression):
    with pytest.raises(TypeError):
        Iteration(..., expression)


def test_constructor_error_expression(alias):
    with pytest.raises(TypeError):
        Iteration(alias, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
