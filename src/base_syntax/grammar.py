from .__external__ import tree
from . import lexis


tokens = lexis.tokens

precedence = (
    ('right', '='),
    ('right', 'QUANTIFIER'),
    ('left', 'IS', 'AS', 'IN'),
    ('left', 'AND', 'OR'),
    ('left', 'COMPARE_TYPE'),
    ('right', 'NOT'),
    ('left', '.'),
    ('right', ')', '(')
)

def p_empty(p):
    'empty : '
    pass

def p_reference_alias(p):
    'reference_alias : "@" NAME'
    p[0] = tree.Alias(p[2])

def p_reference_parameter(p):
    'reference_parameter : "%" NAME'
    p[0] = tree.Parameter(p[2])

def p_reference_field(p):
    'reference_field : NAME'
    p[0] = tree.Field(p[1])

def p_reference_kwarg(p):
    'reference_kwarg : NAME'
    p[0] = tree.Kwarg(p[1])

def p_definition_alias_assignment(p):
    'alias_assignment : expression AS reference_alias'
    p[0] = tree.AliasAssignment(p[1], p[3])

def p_definition_iteration(p):
    'iteration : reference_alias IN expression'
    p[0] = tree.Iteration(p[1], p[3])

def p_definition_field_assignment(p):
    'field_assignment : reference_field "=" expression'
    p[0] = tree.FieldAssignment(p[1], p[3])

def p_definition_kwarg_assignment(p):
    'kwarg_assignment : reference_kwarg "=" expression'
    p[0] = tree.KwargAssignment(p[1], p[3])

def p_expression_with_round_brackets(p):
    'expression : "(" expression ")"'
    p[0] = p[2]

def p_obtainment_constant_int(p):
    'constant : INT_NUMBER'
    p[0] = tree.Constant(p[1])

def p_obtainment_constant_string(p):
    'constant : STRING'
    p[0] = tree.Constant(p[1])

def p_obtainment_constant_as_expression(p):
    'expression : constant'
    p[0] = p[1]

def p_obtainment_attribute(p):
    'expression : expression "." NAME'
    p[0] = tree.Attribute(p[1], p[3])

def p_obtainment_alias_value(p):
    'expression : reference_alias'
    p[0] = tree.AliasValue(p[1])

def p_obtainment_parameter_value(p):
    'expression : reference_parameter'
    p[0] = tree.ParameterValue(p[1])

def p_obtainment_kwarg_assignment_set(p):
    '''
        kwarg_assignment_set : kwarg_assignment
        kwarg_assignment_set : kwarg_assignment ',' kwarg_assignment_set
    '''

    p[0] = [p[1]]

    if len(p) == 4:
        p[0] += p[3]

def p_obtainment_function_call(p):
    '''
        expression : NAME "(" kwarg_assignment_set ")"
        expression : NAME "(" empty ")"
    '''

    if not p[3]:
        p[3] = ()

    p[0] = tree.FunctionCall(p[1], *p[3])

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
    'predicate : alias_assignment IS predicate'
    p[0] = tree.DataAccordance(p[1], p[3])

def p_predicate_sequence_accordance(p):
    'predicate : QUANTIFIER iteration IS predicate'
    p[0] = tree.SequenceAccordance(p[1].lower(), p[2], p[4])

def p_predicate_with_round_brackets(p):
    'predicate : "(" predicate ")"'
    p[0] = p[2]

def p_predicate_as_expression(p):
    'expression : predicate'
    p[0] = p[1]

def p_statement_condition(p):
    'condition : IF predicate'
    p[0] = tree.Condition(p[2])

def p_statement_field_assignment_set(p):
    '''
        field_assignment_set : field_assignment
        field_assignment_set : field_assignment field_assignment_set
    '''

    p[0] = [p[1]]

    if len(p) == 3:
        p[0] += p[2]

def p_statement_declaration(p):
    'declaration : GET field_assignment_set'
    p[0] = tree.Declaration(*p[2])

def p_statement_iteration_set(p):
    '''
        iteration_set : iteration
        iteration_set : iteration iteration_set
    '''

    p[0] = [p[1]]

    if len(p) == 3:
        p[0] += p[2]

def p_statement_source(p):
    'source : USE iteration_set'
    p[0] = tree.Source(*p[2])

def p_query_select_query_only_declaration(p):
    'select_query : declaration'
    p[0] = tree.Select(p[1], None, None)

def p_query_select_query_declaration_and_source(p):
    'select_query : declaration source'
    p[0] = tree.Select(p[1], p[2], None)

def p_query_select_query_declaration_and_condition(p):
    'select_query : declaration condition'
    p[0] = tree.Select(p[1], None, p[2])

def p_query_select_query_full(p):
    'select_query : declaration source condition'
    p[0] = tree.Select(p[1], p[2], p[3])

def p_error(t):
    print('\nInput string:')
    print(t.lexer.lexdata)

    print('\nSyntax error at line %s char %s:' % (t.lineno, t.lexpos+1))
    print(t.lexer.lexdata.splitlines()[t.lineno - 1])

    start_line_pos = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    print(' ' * (t.lexpos-start_line_pos-2), '^')

    raise SyntaxError