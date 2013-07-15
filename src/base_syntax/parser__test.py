import pytest

from .__external__ import tree
from .parser import Parser


@pytest.fixture(scope='module')
def parser():
    return Parser()


@pytest.fixture(scope='module')
def completeness_string():
    return '''
        GET
            field_one = @row_a.attr
            field_two = @row_b.attr
            field_three = {TRUE}
        USE
            @row_a IN %input_seq_a
            @row_b IN %input_seq_b
        IF
            @row_a.parent_id == @row_b.id
            AND ALL @item IN @row.seq IS (
                @item.text AS @text IS (
                        FALSE || (321 != (123))
                     && {"not_empty_string"}
                     && NOT FALSE
                     && (@text == "input_seq.seq.text.value")
                )
            )
    '''


@pytest.fixture(scope='module', params=[
    'GET field_one = 2',
    'GET field_one = @item USE @item IN %seq',
    'GET field_one = %seq IF ALL @item IN %seq IS @item > 1',
    'GET field_one = @item USE @item IN %seq IF @item > 1',
    'GET field_one = eq(a=2,b=3)',
    'GET field_one = abs(value=2)',
    'GET field_one = rand()'
])
def input_select_string(request):
    return request.param


@pytest.fixture(scope='module')
def input_bad_string():
    return 'GET $@row = %param'


def test_constructor(parser):
    assert isinstance(parser, Parser)


def test_parse_ok_realization(parser, completeness_string):
    node = parser.parse(completeness_string, debug=True)

    assert isinstance(node, tree.Select)


def test_parse_ok_select(parser, input_select_string):
    node = parser.parse(input_select_string, debug=True)

    assert isinstance(node, tree.Select)


def test_parse_error_syntax(parser, input_bad_string):
    with pytest.raises(SyntaxError):
        parser.parse(input_bad_string, debug=True)
