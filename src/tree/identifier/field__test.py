import pytest

from .field import Field


@pytest.fixture(scope='module')
def instance(field):
    return field


def test_constructor(instance):
    assert isinstance(instance, Field)


def test_str(instance):
    assert isinstance(str(instance), str)
