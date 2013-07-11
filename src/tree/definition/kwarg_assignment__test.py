import pytest

from .kwarg_assignment import KwargAssignment


@pytest.fixture(scope='module')
def instance(kwarg_assignment):
    return kwarg_assignment


def test_constructor_ok(instance):
    assert isinstance(instance, KwargAssignment)


def test_constructor_error_kwarg(expression):
    with pytest.raises(TypeError):
        KwargAssignment(..., expression)


def test_constructor_error_expression(kwarg):
    with pytest.raises(TypeError):
        KwargAssignment(kwarg, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
