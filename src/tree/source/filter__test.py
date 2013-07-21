import pytest

from .filter import Filter


@pytest.fixture(scope='module')
def instance(filter):
    return filter


def test_constructor_ok(instance):
    assert isinstance(instance, Filter)


def test_constructor_error_source(predicate):
    with pytest.raises(TypeError):
        Filter(..., predicate)


def test_constructor_error_predicate(source):
    with pytest.raises(TypeError):
        Filter(source, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
