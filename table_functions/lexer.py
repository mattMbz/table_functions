from re import match, fullmatch
from table_functions.token import Token, TokenType, lookup_token_type

class Lexer:
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()
    ## End of __init__
    

    def next_token(self) -> Token:
        self._skip_whitespace()

        if match(r'^=$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.EQ)
            else:
                token = Token(TokenType.ASSIGN, self._character)

        elif match(r'^\+$', self._character):
            token = Token(TokenType.PLUS, self._character)

        elif match(r'^$', self._character):
            token = Token(TokenType.EOF, self._character)

        elif match(r'^\($', self._character):
            token = Token(TokenType.LPAREN, self._character)

        elif match(r'^\)$', self._character):
            token = Token(TokenType.RPAREN, self._character)

        elif match(r'^{$', self._character):
            token = Token(TokenType.LBRACE, self._character)

        elif match(r'^}$', self._character):
            token = Token(TokenType.RBRACE, self._character)

        elif match(r'^,$', self._character):
            token = Token(TokenType.COMMA, self._character)

        elif match(r'^;$', self._character):
            token = Token(TokenType.SEMICOLON, self._character)

        elif match(r'^-$', self._character):
            token = Token(TokenType.MINUS, self._character)

        elif match(r'^/$', self._character):
            token = Token(TokenType.DIVISION, self._character)

        elif match(r'^\*$', self._character):
            token = Token(TokenType.MULTIPLICATION, self._character)

        elif match(r'^<$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.LE)
            else:
                token = Token(TokenType.LT, self._character)

        elif match(r'^>$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.GE)
            else:
                token = Token(TokenType.GT, self._character)

        elif match(r'^!$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.NOT_EQ)
            else:
                token = Token(TokenType.NEGATION, self._character)

        elif self._is_letter(self._character):
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)
            return Token(token_type, literal)
        
        elif self._is_number(self._character):
            literal = self._read_number()
            return Token(TokenType.INT, literal)

        else:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token
    # End of next_token()


    def _is_letter(self, character: str) -> bool:
        expresion_regular = r'^[a-zA-Z_][a-zA-Z_]*$'
        return bool(fullmatch(expresion_regular, character))


    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))


    def _make_two_character_token(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character()
        suffix = self._character

        return Token(token_type, f'{prefix}{suffix}')

    
    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else: 
            self._character = self._source[self._read_position]
        
        self._position = self._read_position
        self._read_position += 1
    ## End of _read_character


    def _read_identifier(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character):
            self._read_character()
        
        return self._source[initial_position : self._position]
    # End of _read_identifier
    

    def _read_number(self) -> str:
        initial_position = self._position

        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position]
    # End of _read_number()


    def _peek_character(self) -> str:
        ''' Explore the next character '''
        if self._read_position >= len(self._source):
            return ''

        return self._source[self._read_position]
    # END of _peek_characeter()


    def _skip_whitespace(self) -> None:
        while match(r'^\s$', self._character):
            self._read_character()
    # End of _skip_whitespace