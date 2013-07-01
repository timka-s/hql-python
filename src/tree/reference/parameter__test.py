import pytest

from .parameter import Parameter


@pytest.fixture(scope='module')
def instance(parameter):
    return parameter


def test_constructor(instance):
    assert isinstance(instance, Parameter)


def test_str(instance):
    assert isinstance(str(instance), str)
