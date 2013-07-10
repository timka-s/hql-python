import pytest

from .field_assignment import FieldAssignment


@pytest.fixture(scope='module')
def instance(field_assignment):
    return field_assignment


def test_constructor_ok(instance):
    assert isinstance(instance, FieldAssignment)


def test_constructor_error_field(expression):
    with pytest.raises(TypeError):
        FieldAssignment(..., expression)


def test_constructor_error_expression(field):
    with pytest.raises(TypeError):
        FieldAssignment(field, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
