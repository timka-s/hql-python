import pytest

from .__external__ import tree
from .python_lambda import PythonLambda


@pytest.fixture(scope='module')
def completeness_skip_set():
    return frozenset([
        'Node', 'NodeSet',
        'Identifier', 'Definition', 'Expression', 'Predicate',
            'Source', 'Statement', 'Query',
        'Alias', 'Parameter', 'Field', 'Kwarg',
        'AliasAssignment', 'Iteration', 'FieldAssignment',
            'KwargAssignment',
    ])


@pytest.fixture(scope='module')
def completeness_env():
    node = tree.Select(
        tree.Declaration(
            tree.FieldAssignment(
                tree.Field('num_field'),
                tree.Arithmetic(
                    '*',
                    tree.AliasValue(
                        tree.Alias('numbers__row')
                    ),
                    tree.Constant(3)
                )
            ),
            tree.FieldAssignment(
                tree.Field('field_one'),
                tree.Attribute(
                    tree.AliasValue(
                        tree.Alias('items__row')
                    ),
                    'attr_one'
                )
            ),
            tree.FieldAssignment(
                tree.Field('field_two'),
                tree.FunctionCall(
                    'bool',
                    tree.KwargAssignment(
                        tree.Kwarg('x'),
                        tree.Attribute(
                            tree.AliasValue(
                                tree.Alias('items__row')
                            ),
                            'attr_two'
                        )
                    )
                )
            ),
            tree.FieldAssignment(
                tree.Field('field_three'),
                tree.Verity(
                    tree.TRUE()
                )
            ),
        ),
        tree.Input(
            tree.Filter(
                tree.Combination(
                    tree.Origin(
                        tree.Iteration(
                            tree.Alias('items__row'),
                            tree.ParameterValue(
                                tree.Parameter('items')
                            )
                        )
                    ),
                    tree.Filter(
                        tree.Origin(
                            tree.Iteration(
                                tree.Alias('numbers__row'),
                                tree.ParameterValue(
                                    tree.Parameter('numbers')
                                )
                            )
                        ),
                        tree.Compare(
                            '<',
                            tree.AliasValue(
                                tree.Alias('numbers__row')
                            ),
                            tree.Constant(2)
                        )
                    )
                ),
                tree.SequenceAccordance(
                    'each',
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
                            tree.CheckValue(
                                tree.Constant('some_string')
                            ),
                            tree.Or(
                                tree.FALSE(),
                                tree.Compare(
                                    '!=',
                                    tree.Constant(321),
                                    tree.Constant(123)
                                ),
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
    )

    SN = PythonLambda.Record

    parameters = {
        'numbers': [-1, 1, 2, 3, 4],
        'items': [
            SN({
                'attr_one': 'some_text',
                'attr_two': 'bool()==True',
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
        SN({
            'num_field': -3,
            'field_one': 'some_text',
            'field_two': True,
            'field_three': True
        }),
        SN({
            'num_field': 3,
            'field_one': 'some_text',
            'field_two': True,
            'field_three': True
        })
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


def test_visit_Arithmetic_error_unknown_operator():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.Arithmetic._create([..., ..., ...]))


def test_visit_Compare_error_unknown_comparison():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.Compare._create([..., ..., ...]))


def test_visit_SequenceAccordance_error_unknown_quantifier():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.SequenceAccordance._create([..., ..., ...]))


def test_visit_FunctionCall_error_unknown_name():
    with pytest.raises(NotImplementedError):
        PythonLambda(tree.FunctionCall('not_exists_function'))
