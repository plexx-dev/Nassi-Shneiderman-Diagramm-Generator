"""Private definitions for Token class used by the Lexer"""

import logging
import re

from enum import IntEnum
from typing import Union

NUMERIC_CONSTANT_PATTERN = re.compile(r"""([0-9]+)|(true)|(false)""")
KEYWORD_PATTERN = re.compile(r"""(return)|(continue)|(break)|(new)""")
STRING_LITERAL_PATTERN = re.compile(r"""('|\")(.*)(\"|')""")
MATH_OP_PATTERN = re.compile(r"""\+|-|\*|/|<|>""")

class Token_type(IntEnum):
    UNKNOWN=-1 #maybe this should be renamed to IDENTIFIERs
    LEFT_PAREN=0,
    RIGTH_PAREN=1,
    LEFT_CURLY=2,
    RIGHT_CURLY=3,
    LEFT_BRACKET=4,
    RIGHT_BRACKET=5,
    COMMA=6,
    EQUAL_SIGN=7,
    SEMICOLON=8
    MATH_OP=9
    NUMERIC_CONSTANT=10,
    IF_STATEMENT=11,
    ELSE_STATEMENT=12,
    WHILE_STATEMENT=13,
    DO_WHILE_STATEMENT=14,
    FOR_STATEMENT=15,
    KEY_WORD=16,
    STRING_LITERAL=17
    TYPE_NAME=18

class Token:
    def __init__(self, type: Token_type, content: Union[str, None]=None) -> None:
        self.type = type
        self.content = content

    def __str__(self) -> str:
        if self.content:
            return f"{str(self.type)}: {self.content}"
        return f"{self.type}"

def make_token(tag: str, type_name_pattern:re.Pattern) -> Token:
    if tag == '(':
        return Token(Token_type.LEFT_PAREN, tag)
    elif tag == ')':
        return Token(Token_type.RIGTH_PAREN, tag)
    elif tag == '{':
        return Token(Token_type.LEFT_CURLY, tag)
    elif tag == '}':
        return Token(Token_type.RIGHT_CURLY, tag)
    elif tag == '[':
        return Token(Token_type.LEFT_BRACKET, tag)
    elif tag == ']':
        return Token(Token_type.RIGHT_BRACKET, tag)
    elif tag == ',':
        return Token(Token_type.COMMA, tag)
    elif tag == '=':
        return Token(Token_type.EQUAL_SIGN, tag)
    elif tag == ';':
        return Token(Token_type.SEMICOLON, tag)
    elif MATH_OP_PATTERN.match(tag):
        return Token(Token_type.MATH_OP, tag)
    elif NUMERIC_CONSTANT_PATTERN.match(tag):
        return Token(Token_type.NUMERIC_CONSTANT, tag)
    elif tag == "if":
        return Token(Token_type.IF_STATEMENT, tag)
    elif tag == "else":
        return Token(Token_type.ELSE_STATEMENT, tag)
    elif tag == "while":
        return Token(Token_type.WHILE_STATEMENT, tag)
    elif tag == "do":
        return Token(Token_type.DO_WHILE_STATEMENT, tag)
    elif tag == "for":
        return Token(Token_type.FOR_STATEMENT, tag)
    elif KEYWORD_PATTERN.match(tag):
        return Token(Token_type.KEY_WORD, tag)
    elif STRING_LITERAL_PATTERN.match(tag):
        return Token(Token_type.STRING_LITERAL, tag)
    elif type_name_pattern.match(tag):
        return Token(Token_type.TYPE_NAME, tag)
    else:
        logging.info(f"found unknown token {tag}... Function or variable name?")
        return Token(Token_type.UNKNOWN, tag)