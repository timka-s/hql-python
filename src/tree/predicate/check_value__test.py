import pytest

from .check_value import CheckValue


@pytest.fixture(scope='module')
def instance(check_value):
    return check_value


def test_constructor_ok(instance):
    assert isinstance(instance, CheckValue)


def test_constructor_error_expression(expression):
    with pytest.raises(TypeError):
        CheckValue(...)


def test_str(instance):
    assert isinstance(str(instance), str)
