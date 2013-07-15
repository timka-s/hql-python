import pytest

from .function_call import FunctionCall


@pytest.fixture(scope='module')
def instance(function_call):
    return function_call


def test_constructor_ok(instance):
    assert isinstance(instance, FunctionCall)


def test_constructor_ok_kwarg_assignment_set_empty():
    instance = FunctionCall('func_name')

    assert isinstance(instance, FunctionCall)


def test_constructor_error_name(kwarg_assignment):
    with pytest.raises(TypeError):
        FunctionCall(..., kwarg_assignment)


def test_constructor_error_kwarg_assignment(kwarg_assignment):
    with pytest.raises(TypeError):
        FunctionCall('func_name', kwarg_assignment, ...)


def test_constructor_error_duplicated_kwarg(kwarg_assignment):
    with pytest.raises(ValueError):
        FunctionCall('func_name', kwarg_assignment, kwarg_assignment)


def test_str(instance):
    assert isinstance(str(instance), str)
