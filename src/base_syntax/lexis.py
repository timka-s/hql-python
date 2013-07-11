reserved = {
    'get': 'GET',
    'use': 'USE',
    'if': 'IF',

    'as': 'AS',
    'in': 'IN',

    'any': 'QUANTIFIER',
    'all': 'QUANTIFIER',

    'true': 'TRUE',
    'false': 'FALSE',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'is': 'IS'
}

t_AND = r'\&\&'
t_OR = r'\|\|'

t_COMPARE_TYPE = r'\!=|==|>|<|>=|<='

def t_NAME(t):
    r'[_a-zA-Z][a-zA-Z_]*'
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), 'NAME')
    return t

def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"]|(?<=\\)")*"'
    t.value = t.value[1:-1].replace('\\"', '"')
    return t

tokens = (
    'COMPARE_TYPE',
    'NAME', 'INT_NUMBER', 'STRING',
) + tuple(set(reserved.values()))

literals = '(){}@%.='

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('\nSkipped line %s char %s:' % (t.lineno, t.lexpos+1))
    print(t.lexer.lexdata.splitlines()[t.lineno - 1])
    print(' ' * (t.lexpos-1), '^')

    t.lexer.skip(1)
