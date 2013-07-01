import pytest

from .. import tree


@pytest.fixture(scope='module')
def node():
    return tree.Node._create(tuple())


@pytest.fixture(scope='module')
def node_set(node):
    return tree.NodeSet(tree.Node, [node])
