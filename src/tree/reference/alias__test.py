import pytest

from .alias import Alias


@pytest.fixture(scope='module')
def instance(alias):
    return alias


def test_constructor(instance):
    assert isinstance(instance, Alias)


def test_str(instance):
    assert isinstance(str(instance), str)
