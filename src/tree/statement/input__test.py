import pytest

from .input import Input


@pytest.fixture(scope='module')
def instance(input):
    return input


def test_constructor_ok(instance):
    assert isinstance(instance, Input)


def test_constructor_error_source(source):
    with pytest.raises(TypeError):
        Input(...)


def test_str(instance):
    assert isinstance(str(instance), str)
