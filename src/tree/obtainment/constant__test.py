import pytest

from .constant import Constant


@pytest.fixture(scope='module')
def instance(constant):
    return constant


def test_constructor(instance):
    assert isinstance(instance, Constant)


def test_hash_for_hashable_data(instance):
    assert hash(instance)


def test_hash_for_unhashable_data():
    assert hash(Constant([1,2,3]))


def test_str(instance):
    assert isinstance(str(instance), str)
