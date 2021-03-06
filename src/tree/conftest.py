import pytest

from .. import tree


@pytest.fixture(scope='module')
def node():
    return tree.Node._create(tuple())


@pytest.fixture(scope='module')
def node_set(node):
    return tree.NodeSet(tree.Node, [node])


@pytest.fixture(scope='module')
def identifier():
    return tree.Identifier('reference_name')


@pytest.fixture(scope='module')
def definition():
    return tree.Definition._create(tuple())


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
def source():
    return tree.Source._create(tuple())


@pytest.fixture(scope='module')
def statement():
    return tree.Statement._create(tuple())


@pytest.fixture(scope='module')
def query():
    return tree.Query._create(tuple())


@pytest.fixture(scope='module')
def alias():
    return tree.Alias('alias_name')


@pytest.fixture(scope='module')
def parameter():
    return tree.Parameter('parameter_name')


@pytest.fixture(scope='module')
def field():
    return tree.Field('field_name')


@pytest.fixture(scope='module')
def kwarg():
    return tree.Kwarg('kwarg_name')


@pytest.fixture(scope='module')
def alias_assignment(expression, alias):
    return tree.AliasAssignment(expression, alias)


@pytest.fixture(scope='module')
def iteration(alias, expression):
    return tree.Iteration(alias, expression)


@pytest.fixture(scope='module')
def field_assignment(field, expression):
    return tree.FieldAssignment(field, expression)


@pytest.fixture(scope='module')
def kwarg_assignment(kwarg, expression):
    return tree.KwargAssignment(kwarg, expression)


@pytest.fixture(scope='module')
def constant():
    return tree.Constant('constant')


@pytest.fixture(scope='module')
def attribute(expression):
    return tree.Attribute(expression, 'attribute_name')


@pytest.fixture(scope='module')
def alias_value(alias):
    return tree.AliasValue(alias)


@pytest.fixture(scope='module')
def parameter_value(parameter):
    return tree.ParameterValue(parameter)


@pytest.fixture(scope='module')
def function_call(kwarg_assignment):
    return tree.FunctionCall('func_name', kwarg_assignment)


@pytest.fixture(scope='module')
def verity(predicate):
    return tree.Verity(predicate)


@pytest.fixture(scope='module', params=tree.Arithmetic.__operators__)
def arithmetic(request, expression):
    return tree.Arithmetic(request.param, expression, expression)


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


@pytest.fixture(scope='module', params=tree.Compare.__comparisons__)
def compare(request, expression):
    return tree.Compare(request.param, expression, expression)


@pytest.fixture(scope='module')
def data_accordance(alias_assignment, predicate):
    return tree.DataAccordance(alias_assignment, predicate)


@pytest.fixture(scope='module', params=tree.SequenceAccordance.__quantifiers__)
def sequence_accordance(request, iteration, predicate):
    return tree.SequenceAccordance(request.param, iteration, predicate)


@pytest.fixture(scope='module')
def check_value(expression):
    return tree.CheckValue(expression)


@pytest.fixture(scope='module')
def origin(iteration):
    return tree.Origin(iteration)


@pytest.fixture(scope='module')
def filter(source, predicate):
    return tree.Filter(source, predicate)


@pytest.fixture(scope='module')
def combination(source):
    return tree.Combination(source, source)


@pytest.fixture(scope='module')
def declaration(field_assignment):
    return tree.Declaration(field_assignment)


@pytest.fixture(scope='module')
def input(source):
    return tree.Input(source)


@pytest.fixture(scope='module')
def select(declaration, input):
    return tree.Select(declaration, input)
