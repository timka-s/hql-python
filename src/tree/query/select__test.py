import pytest

from .select import Select


@pytest.fixture(scope='module')
def instance(select):
    return select


def test_constructor_ok(instance):
    assert isinstance(instance, Select)


def test_constructor_ok_just_declaration(declaration):
    assert isinstance(Select(declaration), Select)


def test_constructor_error_declaration(source, condition):
    with pytest.raises(TypeError):
        Select(..., source, condition)


def test_constructor_error_source(declaration, condition):
    with pytest.raises(TypeError):
        Select(declaration, ..., condition)


def test_constructor_error_condition(declaration, source):
    with pytest.raises(TypeError):
        Select(declaration, source, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
