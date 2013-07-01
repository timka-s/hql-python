import pytest

from .data_accordance import DataAccordance


@pytest.fixture
def instance(data_accordance):
    return data_accordance


def test_constructor_ok(instance):
    assert isinstance(instance, DataAccordance)


def test_constructor_error_alias_assignment(predicate):
    with pytest.raises(TypeError):
        DataAccordance(..., predicate)


def test_constructor_error_predicate(alias_assignment):
    with pytest.raises(TypeError):
        DataAccordance(alias_assignment, ...)


def test_str(instance):
    assert isinstance(str(instance), str)
