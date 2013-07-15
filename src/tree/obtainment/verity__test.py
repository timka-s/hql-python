import pytest

from .verity import Verity


@pytest.fixture(scope='module')
def instance(verity):
    return verity


def test_constructor_ok(instance):
    assert isinstance(instance, Verity)


def test_constructor_error_predicate():
    with pytest.raises(TypeError):
        Verity(...)


def test_str(instance):
    assert isinstance(str(instance), str)
