import pytest

from .condition import Condition


@pytest.fixture(scope='module')
def instance(condition):
    return condition


def test_constructor_ok(instance):
    assert isinstance(instance, Condition)


def test_constructor_error_predicate():
    with pytest.raises(TypeError):
        Condition(...)


def test_str(instance):
    assert isinstance(str(instance), str)
