import pytest

from .origin import Origin


@pytest.fixture(scope='module')
def instance(origin):
    return origin


def test_constructor_ok(instance):
    assert isinstance(instance, Origin)


def test_constructor_error_iteration():
    with pytest.raises(TypeError):
        Origin(...)


def test_str(instance):
    assert isinstance(str(instance), str)
