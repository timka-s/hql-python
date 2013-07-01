import pytest

from .bool_complex import Complex


@pytest.fixture(scope='module')
def instance(predicate_a, predicate_b):
    return Complex(predicate_a, predicate_b)


def test_constructor(instance):
    assert isinstance(instance, Complex)


def test_constructor_ok_one(predicate_a):
    assert Complex(predicate_a) is predicate_a


def test_constructor_ok_many(predicate_a, predicate_b, predicate_c):
    first = Complex(predicate_a, predicate_b)
    second = Complex(predicate_b, predicate_c)

    instance_from_merge = Complex(first, second)
    instance_from_direct = Complex(predicate_a, predicate_b, predicate_c)

    assert instance_from_merge == instance_from_direct


def test_constructor_error_empty():
    with pytest.raises(ValueError):
        Complex()


def test_constructor_error_predicate(predicate_a, predicate_b):
    with pytest.raises(TypeError):
        Complex(predicate_a, ..., predicate_b)


def test_str(instance):
    assert isinstance(str(instance), str)
