import pytest

from .bool_true import TRUE


@pytest.fixture(scope='module')
def instance(bool_true):
    return bool_true


def test_constructor(instance):
    assert isinstance(instance, TRUE)


def test_str(instance):
    assert isinstance(str(instance), str)
