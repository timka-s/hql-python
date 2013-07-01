import pytest

from .alias_assignment import AliasAssignment


@pytest.fixture(scope='module')
def instance(alias_assignment):
    return alias_assignment


def test_constructor_ok(instance):
    assert isinstance(instance, AliasAssignment)


def test_constructor_error_expression(alias):
    with pytest.raises(TypeError):
        AliasAssignment(..., alias)


def test_constructor_error_alias(expression):
    with pytest.raises(TypeError):
        AliasAssignment(expression, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
