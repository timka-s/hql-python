import pytest

from .source import Source


@pytest.fixture(scope='module')
def instance(source):
    return source


def test_constructor_ok(instance):
    assert isinstance(instance, Source)


def test_constructor_error_empty():
    with pytest.raises(ValueError):
        Source()


def test_constructor_error_iteration(iteration):
    with pytest.raises(TypeError):
        Source(iteration, ...)


def test_constructor_error_duplicated_alias(iteration):
    with pytest.raises(ValueError):
        Source(iteration, iteration)


def test_str(instance):
    assert isinstance(str(instance), str)
