import pytest

from .identifier import Identifier


@pytest.fixture(scope='module')
def instance(identifier):
    return identifier


def test_constructor_ok(instance):
    assert isinstance(instance, Identifier)


def test_constructor_error_name():
    with pytest.raises(TypeError):
        Identifier(...)


def test_str(instance):
    assert isinstance(str(instance), str)
