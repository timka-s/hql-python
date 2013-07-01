import pytest

from .bool_or import Or


@pytest.fixture(scope='module')
def instance(bool_or):
    return bool_or


def test_constructor(instance):
    assert isinstance(instance, Or)


def test_str(instance):
    assert isinstance(str(instance), str)
