import pytest

from .. import tree


@pytest.fixture(scope='module')
def node():
    return tree.Node._create(tuple())


@pytest.fixture(scope='module')
def node_set(node):
    return tree.NodeSet(tree.Node, [node])


@pytest.fixture(scope='module')
def expression():
    return tree.Expression._create(tuple())


@pytest.fixture(scope='module')
def predicate():
    return tree.Predicate._create(tuple())


@pytest.fixture(scope='module')
def predicate_a():
    return tree.Predicate._create('a')


@pytest.fixture(scope='module')
def predicate_b():
    return tree.Predicate._create('b')


@pytest.fixture(scope='module')
def predicate_c():
    return tree.Predicate._create('c')


@pytest.fixture(scope='module')
def obtainment():
    return tree.Obtainment._create(tuple())


@pytest.fixture(scope='module')
def bool_true():
    return tree.TRUE()


@pytest.fixture(scope='module')
def bool_false():
    return tree.FALSE()


@pytest.fixture(scope='module')
def bool_not(predicate):
    return tree.Not(predicate)


@pytest.fixture(scope='module')
def bool_and(predicate_a, predicate_b):
    return tree.And(predicate_a, predicate_b)


@pytest.fixture(scope='module')
def bool_or(predicate_a, predicate_b):
    return tree.Or(predicate_a, predicate_b)


@pytest.fixture(scope='module')
def constant():
    return tree.Constant('constant')


@pytest.fixture(scope='module')
def attribute(expression):
    return tree.Attribute(expression, 'attribute_name')
