import pytest

from .alias_value import AliasValue


@pytest.fixture(scope='module')
def instance(alias_value):
    return alias_value


def test_constructor_ok(instance):
    assert isinstance(instance, AliasValue)


def test_constructor_error_alias():
    with pytest.raises(TypeError):
        AliasValue(...)


def test_str(instance):
    assert isinstance(str(instance), str)
