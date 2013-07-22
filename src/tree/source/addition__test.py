import pytest

from .addition import Addition


@pytest.fixture(scope='module')
def instance(addition):
    return addition


def test_constructor_ok(instance):
    assert isinstance(instance, Addition)


def test_constructor_error_empty():
    with pytest.raises(ValueError):
        Addition()


def test_constructor_error_one(source):
    with pytest.raises(ValueError):
        Addition(source)


def test_constructor_error_source(source):
    with pytest.raises(TypeError):
        Addition(source, ..., source)


def test_str(instance):
    assert isinstance(str(instance), str)
