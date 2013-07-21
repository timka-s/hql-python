import pytest

from .select import Select


@pytest.fixture(scope='module')
def instance(select):
    return select


def test_constructor_ok(instance):
    assert isinstance(instance, Select)


def test_constructor_ok_just_declaration(declaration):
    assert isinstance(Select(declaration), Select)


def test_constructor_error_declaration(input):
    with pytest.raises(TypeError):
        Select(..., input)


def test_constructor_error_input(declaration):
    with pytest.raises(TypeError):
        Select(declaration, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
