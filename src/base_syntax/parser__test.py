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
        USING SUCH COMBINATION
            SUCH @row_a FROM %input_seq_a WHERE @row_a.field > 22
            @row_b FROM %input_seq_b
        WHERE
            @row_a.parent_id == @row_b.id
            AND EACH @item FROM @row.seq ACCORD (
                @item.text AS @text ACCORD (
                        FALSE || (321 != (123))
                     && {"not_empty_string"}
                     && NOT FALSE
                     && (@text == "input_seq.seq.text.value")
                )
            )
    '''


@pytest.fixture(scope='module', params=[
    'GET field_one = 2',
    'GET field_one = @item USING @item FROM %seq',
    'GET field_one = @item USING SUCH @item FROM %seq WHERE @item > 1',
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
