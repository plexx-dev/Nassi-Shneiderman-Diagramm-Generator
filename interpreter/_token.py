"""Private definitions for Token class used by the Lexer"""

import re
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Union

NUMERIC_CONSTANT_PATTERN = re.compile(r"""([0-9]+)|(true)|(false)""")
KEYWORD_PATTERN = re.compile(r"""(return)$|(continue)$|(break)$|(new)$""")
STRING_LITERAL_PATTERN = re.compile(r"""('|\")(.*)(\"|')""")
MATH_OP_PATTERN = re.compile(r"""\+|-|\*|/|<|>""")

class Token_type(IntEnum):
    UNKNOWN=-1 #maybe this should be renamed to IDENTIFIER
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

@dataclass(frozen=True)
class SourceLocation:
    file: str
    line: int
    column: int

    def __str__(self) -> str:
        return f"File {self.file} {self.line}:{self.column}"

@dataclass(frozen=True, eq=True)
class Token:
    type: Token_type
    location: SourceLocation = field(compare=False, default=SourceLocation("", 0, 0))
    content: str = field(compare=False, default="")

def make_token(tag: str, location: SourceLocation, type_name_pattern:re.Pattern) -> Token:
    """Construct a token object with the provided tag and source location"""
    if tag == '(':
        return Token(Token_type.LEFT_PAREN, location, tag)
    elif tag == ')':
        return Token(Token_type.RIGTH_PAREN, location, tag)
    elif tag == '{':
        return Token(Token_type.LEFT_CURLY, location, tag)
    elif tag == '}':
        return Token(Token_type.RIGHT_CURLY, location, tag)
    elif tag == '[':
        return Token(Token_type.LEFT_BRACKET, location, tag)
    elif tag == ']':
        return Token(Token_type.RIGHT_BRACKET, location, tag)
    elif tag == ',':
        return Token(Token_type.COMMA, location, tag)
    elif tag == '=':
        return Token(Token_type.EQUAL_SIGN, location, tag)
    elif tag == ';':
        return Token(Token_type.SEMICOLON, location, tag)
    elif MATH_OP_PATTERN.match(tag):
        return Token(Token_type.MATH_OP, location, tag)
    elif NUMERIC_CONSTANT_PATTERN.match(tag):
        return Token(Token_type.NUMERIC_CONSTANT, location, tag)
    elif tag == "if":
        return Token(Token_type.IF_STATEMENT, location, tag)
    elif tag == "else":
        return Token(Token_type.ELSE_STATEMENT, location, tag)
    elif tag == "while":
        return Token(Token_type.WHILE_STATEMENT, location, tag)
    elif tag == "do":
        return Token(Token_type.DO_WHILE_STATEMENT, location, tag)
    elif tag == "for":
        return Token(Token_type.FOR_STATEMENT, location, tag)
    elif KEYWORD_PATTERN.match(tag):
        return Token(Token_type.KEY_WORD, location, tag)
    elif STRING_LITERAL_PATTERN.match(tag):
        return Token(Token_type.STRING_LITERAL, location, tag)
    elif type_name_pattern.match(tag):
        return Token(Token_type.TYPE_NAME, location, tag)
    else:
        return Token(Token_type.UNKNOWN, location, tag)