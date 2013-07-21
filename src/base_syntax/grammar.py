from .__external__ import tree
from . import lexis


tokens = lexis.tokens

precedence = (
    ('right', '='),
    ('right', 'QUANTIFIER'),
    ('left', 'ACCORD', 'AS', 'FROM'),
    ('left', 'AND', 'OR'),
    ('left', 'COMPARE_TYPE'),
    ('right', 'NOT'),
    ('left', '.'),
    ('right', ')', '(')
)

def p_empty(p):
    'empty : '
    pass

def p_identifier_alias(p):
    'identifier_alias : "@" NAME'
    p[0] = tree.Alias(p[2])

def p_identifier_parameter(p):
    'identifier_parameter : "%" NAME'
    p[0] = tree.Parameter(p[2])

def p_identifier_field(p):
    'identifier_field : NAME'
    p[0] = tree.Field(p[1])

def p_identifier_kwarg(p):
    'identifier_kwarg : NAME'
    p[0] = tree.Kwarg(p[1])

def p_definition_alias_assignment(p):
    'alias_assignment : expression AS identifier_alias'
    p[0] = tree.AliasAssignment(p[1], p[3])

def p_definition_iteration(p):
    'iteration : identifier_alias FROM expression'
    p[0] = tree.Iteration(p[1], p[3])

def p_definition_field_assignment(p):
    'field_assignment : identifier_field "=" expression'
    p[0] = tree.FieldAssignment(p[1], p[3])

def p_definition_kwarg_assignment(p):
    'kwarg_assignment : identifier_kwarg "=" expression'
    p[0] = tree.KwargAssignment(p[1], p[3])

def p_expression_with_round_brackets(p):
    'expression : "(" expression ")"'
    p[0] = p[2]

def p_expression_constant_int(p):
    'constant : INT_NUMBER'
    p[0] = tree.Constant(p[1])

def p_expression_constant_string(p):
    'constant : STRING'
    p[0] = tree.Constant(p[1])

def p_expression_from_constant(p):
    'expression : constant'
    p[0] = p[1]

def p_expression_attribute(p):
    'expression : expression "." NAME'
    p[0] = tree.Attribute(p[1], p[3])

def p_expression_alias_value(p):
    'expression : identifier_alias'
    p[0] = tree.AliasValue(p[1])

def p_expression_parameter_value(p):
    'expression : identifier_parameter'
    p[0] = tree.ParameterValue(p[1])

def p_expression_kwarg_assignment_set(p):
    '''
        kwarg_assignment_set : kwarg_assignment
        kwarg_assignment_set : kwarg_assignment_set ',' kwarg_assignment
    '''

    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_expression_function_call(p):
    '''
        expression : NAME "(" kwarg_assignment_set ")"
        expression : NAME "(" empty ")"
    '''

    if not p[3]:
        p[3] = ()

    p[0] = tree.FunctionCall(p[1], *p[3])

def p_expression_verity(p):
    'expression : "{" predicate "}"'
    p[0] = tree.Verity(p[2])

def p_predicate_true(p):
    'predicate : TRUE'
    p[0] = tree.TRUE()

def p_predicate_false(p):
    'predicate : FALSE'
    p[0] = tree.FALSE()

def p_predicate_not(p):
    'predicate : NOT predicate'
    p[0] = tree.Not(p[2])

def p_predicate_and(p):
    'predicate : predicate AND predicate'
    p[0] = tree.And(p[1], p[3])

def p_predicate_or(p):
    'predicate : predicate OR predicate'
    p[0] = tree.Or(p[1], p[3])

def p_predicate_compare(p):
    'predicate : expression COMPARE_TYPE expression'
    p[0] = tree.Compare(p[2], p[1], p[3])

def p_predicate_data_accordance(p):
    'predicate : alias_assignment ACCORD predicate'
    p[0] = tree.DataAccordance(p[1], p[3])

def p_predicate_sequence_accordance(p):
    'predicate : QUANTIFIER iteration ACCORD predicate'
    p[0] = tree.SequenceAccordance(p[1].lower(), p[2], p[4])

def p_predicate_check_value(p):
    'predicate : "{" expression "}"'
    p[0] = tree.CheckValue(p[2])

def p_predicate_with_round_brackets(p):
    'predicate : "(" predicate ")"'
    p[0] = p[2]

def p_source_origin(p):
    'source : iteration'
    p[0] = tree.Origin(p[1])

def p_source_filter(p):
    'source : SUCH source WHERE predicate'
    p[0] = tree.Filter(p[2], p[4])

def p_source_set(p):
    '''
        source_set : source
        source_set : source_set source
    '''

    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_source_combination(p):
    'source : COMBINATION source_set'
    p[0] = tree.Combination(*p[2])

def p_statement_field_assignment_set(p):
    '''
        field_assignment_set : field_assignment
        field_assignment_set : field_assignment_set field_assignment
    '''

    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_declaration(p):
    'declaration : GET field_assignment_set'
    p[0] = tree.Declaration(*p[2])

def p_statement_input(p):
    'input : USING source'
    p[0] = tree.Input(p[2])

def p_query_select_query_only_declaration(p):
    'select_query : declaration'
    p[0] = tree.Select(p[1], None)

def p_query_select_query_declaration_and_input(p):
    'select_query : declaration input'
    p[0] = tree.Select(p[1], p[2])

def p_error(t):
    print('\nInput string:')
    print(t.lexer.lexdata)

    print('\nSyntax error at line %s char %s:' % (t.lineno, t.lexpos+1))
    print(t.lexer.lexdata.splitlines()[t.lineno - 1])

    start_line_pos = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    print(' ' * (t.lexpos-start_line_pos-2), '^')

    raise SyntaxError
