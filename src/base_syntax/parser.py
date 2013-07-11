from ply.lex import lex
from ply.yacc import yacc

from . import lexis, grammar


class Parser:
    _lexer = lex(module=lexis)

    def __init__(self, start='select_query', debug=False):
        self._parser = yacc(
            debug=debug,
            module=grammar,
            start=start,
            write_tables=False
        )

    def parse(self, string, debug=False):
        return self._parser.parse(
            input=string,
            lexer=self._lexer.clone(),
            debug=debug
        )
