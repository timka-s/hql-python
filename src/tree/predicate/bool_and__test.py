import pytest

from .bool_and import And


@pytest.fixture(scope='module')
def instance(bool_and):
    return bool_and


def test_constructor(instance):
    assert isinstance(instance, And)


def test_str(instance):
    assert isinstance(str(instance), str)
