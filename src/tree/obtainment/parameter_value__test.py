import pytest

from .parameter_value import ParameterValue


@pytest.fixture(scope='module')
def instance(parameter_value):
    return parameter_value


def test_constructor_ok(instance):
    assert isinstance(instance, ParameterValue)


def test_constructor_error_parameter():
    with pytest.raises(TypeError):
        ParameterValue(...)


def test_str(instance):
    assert isinstance(str(instance), str)
