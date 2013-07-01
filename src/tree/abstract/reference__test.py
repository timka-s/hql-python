import pytest

from .reference import Reference


@pytest.fixture(scope='module')
def instance(reference):
    return reference


def test_constructor_ok(instance):
    assert isinstance(instance, Reference)


def test_constructor_error_name():
    with pytest.raises(TypeError):
        Reference(...)


def test_str(instance):
    assert isinstance(str(instance), str)
