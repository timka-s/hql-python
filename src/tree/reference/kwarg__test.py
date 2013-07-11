import pytest

from .kwarg import Kwarg


@pytest.fixture(scope='module')
def instance(kwarg):
    return kwarg


def test_constructor(instance):
    assert isinstance(instance, Kwarg)


def test_str(instance):
    assert isinstance(str(instance), str)
