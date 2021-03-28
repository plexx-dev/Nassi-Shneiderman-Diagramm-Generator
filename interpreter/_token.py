"""Private definitions for Token class used by the Lexer"""

import re

from enum import IntEnum
from typing import Union

NUMERIC_CONSTANT_PATTERN = re.compile("([0-9]+)|(true)|(false)")
KEYWORD_PATTERN = re.compile("(return)|(continue)|(break)")

class Token_type(IntEnum):
    UNKNOWN=-1
    LEFT_PAREN=0,
    RIGTH_PAREN=1,
    LEFT_CURLY=2,
    RIGHT_CURLY=3,
    LEFT_BRACKET=4,
    RIGHT_BRACKET=5,
    COMMA=6,
    NUMERIC_CONSTANT=7,
    IF_STATEMENT=8,
    WHILE_STATEMENT=9,
    DO_WHILE_STATEMENT=10,
    FOR_STATEMENT=11,
    KEY_WORD=13,
    STRING_LITERAL=14

class Token:
    def __init__(self, type: Token_type, content: Union[str, None]=None) -> None:
        self.type = type
        self.content = content

def make_token(tag: str) -> Token:
    if tag == '(':
        return Token(Token_type.LEFT_PAREN)
    elif tag == ')':
        return Token(Token_type.RIGTH_PAREN)
    elif tag == '{':
        return Token(Token_type.LEFT_CURLY)
    elif tag == '}':
        return Token(Token_type.RIGHT_CURLY)
    elif tag == '[':
        return Token(Token_type.LEFT_BRACKET)
    elif tag == ']':
        return Token(Token_type.RIGHT_BRACKET)
    elif tag == ',':
        return Token(Token_type.COMMA)
    elif NUMERIC_CONSTANT_PATTERN.match(tag):
        return Token(Token_type.NUMERIC_CONSTANT, tag)
    elif tag == 'if':
        return Token(Token_type.IF_STATEMENT)
    elif tag == 'while':
        return Token(Token_type.WHILE_STATEMENT)
    elif tag == 'do':
        return Token(Token_type.DO_WHILE_STATEMENT)
    elif tag == 'for':
        return Token(Token_type.FOR_STATEMENT)
    #TODO: finish this