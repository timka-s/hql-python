import pytest

from .sequence_accordance import SequenceAccordance


@pytest.fixture
def instance(sequence_accordance):
    return sequence_accordance


def test_constructor_ok(instance):
    assert isinstance(instance, SequenceAccordance)


def test_constructor_error_quantifier(iteration, predicate):
    with pytest.raises(ValueError):
        SequenceAccordance(..., iteration, predicate)


def test_constructor_error_iteration(predicate):
    with pytest.raises(TypeError):
        SequenceAccordance('any', ..., predicate)


def test_constructor_error_predicate(iteration):
    with pytest.raises(TypeError):
        SequenceAccordance('all', iteration, ...,)


def test_str(instance):
    assert isinstance(str(instance), str)
