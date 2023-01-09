from enum import auto, Enum, unique
from typing import Dict, NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()    # equal assign '='
    AVG = auto()       # find average 'avg()'
    COMMA = auto()     # comma ','
    CREATETABLE = auto() # create new table 'createtable()'
    DIVISION = auto()  # "/"
    ELSE = auto()      # alternative conditional token 'else'
    EOF = auto()       # End Of File
    EQ = auto()        # equal operator '='
    FALSE = auto()     # False token 'falso'
    FUNCTION = auto()  # 'function' Keyword
    GT = auto()        # Greater than operator '>'
    GE = auto()        # Greater than or Equal To '>='
    IDENT = auto()     # identifier: variable names
    IF = auto()        # conditional 'if'
    ILLEGAL = auto()   # when some TOKEN is no idetified
    INT = auto()       # Integer TOKENS
    LBRACE = auto()    # left curly brace "{" 
    LE = auto()        # Less than or equal to "<="
    LET = auto()       # variable definition  'var'
    LPAREN = auto()    # Left parenthesis '('
    LT = auto()        # Less than '<'
    MINUS = auto()     # minus '-'
    MULTIPLICATION = auto() # product '*'
    NEGATION = auto()  # NOT token "!"
    NOT_EQ = auto()    # different to token "!="
    PLUS = auto()      # Plus operator '+'
    POW = auto()       # "Pow", for power calcs
    RBRACE = auto()    # right curly brace '}'
    RETURN = auto()    # function return
    RPAREN = auto()    # right parenthesis ')'
    SEMICOLON = auto() # semicolon ';'
    SUM = auto()       # Add row numbers "var add_1 = salaries.table_1.sum(july);"
    TRUE = auto()      # true token 'verdadero'

# End pf TokenType Class


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'false': TokenType.FALSE,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'var': TokenType.LET,
        'true': TokenType.TRUE 
    }

    return keywords.get(literal, TokenType.IDENT)
## End of lookup_token_type()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'
# End of Token Class