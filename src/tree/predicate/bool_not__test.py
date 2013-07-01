import pytest

from .bool_not import Not


@pytest.fixture(scope='module')
def instance(bool_not):
    return bool_not


def test_constructor_ok(instance):
    assert isinstance(instance, Not)


def test_constructor_ok_double(predicate):
    assert Not(Not(predicate)) is predicate


def test_constructor_error_predicate():
    with pytest.raises(TypeError):
        Not(...)


def test_str(instance):
    assert isinstance(str(instance), str)
