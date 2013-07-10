import pytest

from .__external__ import tree
from .python_lambda import PythonLambda


@pytest.fixture(scope='module')
def completeness_skip_set():
    return frozenset([
        'Node', 'NodeSet',
        'Expression', 'Reference', 'Definition', 'Obtainment', 'Predicate',
            'Statement', 'Query',
        'Alias', 'Parameter', 'Field',
        'AliasAssignment', 'Iteration', 'FieldAssignment'
    ])


@pytest.fixture(scope='module')
def completeness_env():
    node = tree.Select(
        tree.Declaration(
            tree.FieldAssignment(
                tree.Field('field_one'),
                tree.Attribute(
                    tree.AliasValue(
                        tree.Alias('items__row')
                    ),
                    'attr_one'
                )
            )
        ),
        tree.Source(
            tree.Iteration(
                tree.Alias('items__row'),
                tree.ParameterValue(
                    tree.Parameter('items')
                )
            )
        ),
        tree.Condition(
            tree.SequenceAccordance(
                'all',
                tree.Iteration(
                    tree.Alias('items__row__attr_seq'),
                    tree.Attribute(
                        tree.AliasValue(
                            tree.Alias('items__row')
                        ),
                        'attr_seq'
                    )
                ),
                tree.DataAccordance(
                    tree.AliasAssignment(
                        tree.Attribute(
                            tree.AliasValue(
                                tree.Alias('items__row__attr_seq')
                            ),
                            'text'
                        ),
                        tree.Alias('items__row__attr_seq__text')
                    ),
                    tree.And(
                        tree.Or(
                            tree.FALSE(),
                            tree.TRUE()
                        ),
                        tree.Not(tree.FALSE()),
                        tree.Compare(
                            '==',
                            tree.AliasValue(
                                tree.Alias('items__row__attr_seq__text')
                            ),
                            tree.Constant('items.attr_seq.text.value')
                        )
                    )
                )
            )
        )
    )

    SN = PythonLambda.Record

    parameters = {
        'items': [
            SN({
                'attr_one': 'some_text',
                'attr_seq': [
                    SN({'text': 'items.attr_seq.text.value'}),
                    SN({'text': 'items.attr_seq.text.value'})
                ]
            }),
            SN({
                'attr_seq': [
                    SN({'text': 'BAD.items.attr_seq.text.value'}),
                ]
            })
        ]
    }

    result = [
        SN({'field_one': 'some_text'})
    ]

    return node, parameters, result


def test_completeness(tester_visitor_completeness, completeness_skip_set):
    assert tester_visitor_completeness(PythonLambda, completeness_skip_set)


def test_sufficiency(tester_visitor_sufficiency):
    assert tester_visitor_sufficiency(PythonLambda)


def test_realization(completeness_env):
    node, parameters, result = completeness_env

    visitor = PythonLambda(node)

    assert str(visitor.output(parameters)) == str(result)


def test_visit_Compare_error_unknown_comparison():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.Compare._create([..., ..., ...]))


def test_visit_SequenceAccordance_error_unknown_quantifier():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.SequenceAccordance._create([..., ..., ...]))


def test_visit_Source_error_many_iterators():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.Source._create([[..., ...]]))
