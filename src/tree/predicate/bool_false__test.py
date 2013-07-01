import pytest

from .bool_false import FALSE


@pytest.fixture(scope='module')
def instance(bool_false):
    return bool_false


def test_constructor(instance):
    assert isinstance(instance, FALSE)


def test_str(instance):
    assert isinstance(str(instance), str)
