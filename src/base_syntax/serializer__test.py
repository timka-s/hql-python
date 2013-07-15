import pytest

from .__external__ import tree
from .serializer import Serializer


@pytest.fixture(scope='module')
def completeness_skip_set():
    return frozenset([
        'Node', 'NodeSet',
        'Expression', 'Reference', 'Definition', 'Obtainment', 'Predicate',
            'Statement', 'Query',
    ])


@pytest.fixture(scope='module')
def completeness_node():
    return tree.Select(
        tree.Declaration(
            tree.FieldAssignment(
                tree.Field('field_one'),
                tree.CaseValue(
                    tree.Constant('test_case'),
                    tree.Constant('default_result'),
                    tree.WhenAssignment(
                        tree.Attribute(
                            tree.AliasValue(
                                tree.Alias('items__row')
                            ),
                            'attr_one'
                        ),
                        tree.Constant('eq to attr_one result')
                    ),
                ),
            ),
            tree.FieldAssignment(
                tree.Field('field_two'),
                tree.IfValue(
                    tree.Constant(0),
                    tree.IfAssignment(
                        tree.Compare(
                            '==',
                            tree.ParameterValue(
                                tree.Parameter('some_string')
                            ),
                            tree.Constant('some_string')
                        ),
                        tree.Constant(1)
                    ),
                    tree.IfAssignment(
                        tree.Compare(
                            '>',
                            tree.Constant(5),
                            tree.Constant(1)
                        ),
                        tree.Constant(2)
                    ),
                ),
            )
        ),
        tree.Source(
            tree.Iteration(
                tree.Alias('items__row'),
                tree.FunctionCall(
                    'ds',
                    tree.KwargAssignment(
                        tree.Kwarg('name'),
                        tree.ParameterValue(
                            tree.Parameter('ds_name')
                        )
                    )
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
                            tree.TRUE(),
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


def test_completeness(tester_visitor_completeness, completeness_skip_set):
    assert tester_visitor_completeness(Serializer, completeness_skip_set)


def test_sufficiency(tester_visitor_sufficiency):
    assert tester_visitor_sufficiency(Serializer)


def test_realization(completeness_node):
    visitor = Serializer(completeness_node)

    assert isinstance(visitor.output, str)
