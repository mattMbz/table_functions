from unittest import TestCase
from typing import List

from table_functions.token import Token, TokenType
from table_functions.lexer import Lexer

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_illegal()


    def test_one_character_operator(self) -> None:
        source: str = '=+-/*<>!'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.DIVISION, '/'),
            Token(TokenType.MULTIPLICATION, '*'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NEGATION, '!'),
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End test_one_character_operator()


    def test_oef(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source) + 1):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, '')
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_eof()


    def test_delimiters(self) -> None:
        source: str = "(){},;"
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';')
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_delimiters()


    def test_assigment(self) -> None:
        source: str = 'var cinco = 5;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(5):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'var'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_assigment()


    def test_function_call(self) -> None:
        source: str = 'var resultado_sd = suma(dos, tres);'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(4):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'var'),
            Token(TokenType.IDENT, 'resultado_sd'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_function_call()


    def test_control_statement(self) -> None:
        source: str = '''
            if (5 < 10) {
                return true;
            } else {
                return false;
            }
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(17):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.TRUE, 'true'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.FALSE, 'false'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_control_statement()


    def test_two_character_operator(self) -> None:
        source: str = '''
            10 == 10;
            10 != 9;
            5 <= 10;
            5 >= 0;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(16):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.INT, '10'),
            Token(TokenType.EQ, '=='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '10'),
            Token(TokenType.NOT_EQ, '!='),
            Token(TokenType.INT, '9'),
            Token(TokenType.SEMICOLON, ';'),

            Token(TokenType.INT, '5'),
            Token(TokenType.LE, '<='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),

            Token(TokenType.INT, '5'),
            Token(TokenType.GE, '>='),
            Token(TokenType.INT, '0'),
            Token(TokenType.SEMICOLON, ';'),

        ]

        self.assertEquals(tokens, expected_tokens)
    ## End of test_two_character_operator()

## End of LexerText Class