reserved = {
    'get': 'GET',
    'using': 'USING',

    'such': 'SUCH',
    'where': 'WHERE',
    'combination': 'COMBINATION',

    'as': 'AS',
    'from': 'FROM',

    'any': 'QUANTIFIER',
    'each': 'QUANTIFIER',

    'true': 'TRUE',
    'false': 'FALSE',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'accord': 'ACCORD'
}

t_AND = r'\&\&'
t_OR = r'\|\|'

t_COMPARE_TYPE = r'\!=|==|>|<|>=|<='

def t_NAME(t):
    r'[_a-zA-Z][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), 'NAME')
    return t

def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"]|\\")*"' r'|' r"'([^']|\\'')*'"
    quote = t.value[0]
    t.value = t.value[1:-1].replace('\\' + quote, quote)
    return t

tokens = (
    'COMPARE_TYPE',
    'NAME', 'INT_NUMBER', 'STRING',
) + tuple(set(reserved.values()))

literals = '(){}@%.=,'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('\nSkipped line %s char %s:' % (t.lineno, t.lexpos+1))
    print(t.lexer.lexdata.splitlines()[t.lineno - 1])

    start_line_pos = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    print(' ' * (t.lexpos-start_line_pos-2), '^')

    t.lexer.skip(1)
