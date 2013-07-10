import pytest

from .declaration import Declaration


@pytest.fixture(scope='module')
def instance(declaration):
    return declaration


def test_constructor_ok(instance):
    assert isinstance(instance, Declaration)


def test_constructor_error_empty():
    with pytest.raises(ValueError):
        Declaration()


def test_constructor_error_field_assignment(field_assignment):
    with pytest.raises(TypeError):
        Declaration(field_assignment, ...)


def test_constructor_error_duplicated_field(field_assignment):
    with pytest.raises(ValueError):
        Declaration(field_assignment, field_assignment)


def test_str(instance):
    assert isinstance(str(instance), str)
