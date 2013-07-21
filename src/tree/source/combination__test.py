import pytest

from .combination import Combination


@pytest.fixture(scope='module')
def instance(combination):
    return combination


def test_constructor_ok(instance):
    assert isinstance(instance, Combination)


def test_constructor_error_empty():
    with pytest.raises(ValueError):
        Combination()


def test_constructor_error_one(source):
    with pytest.raises(ValueError):
        Combination(source)


def test_constructor_error_source(source):
    with pytest.raises(TypeError):
        Combination(source, ..., source)


def test_str(instance):
    assert isinstance(str(instance), str)
