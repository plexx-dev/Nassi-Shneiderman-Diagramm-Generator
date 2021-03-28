"""Lexer.py: Definition for Lexer class"""

import logging
import re
from typing import List, overload

from interpreter.function_scope import Function_scope
from interpreter._token import Token, make_token
class Lexer:
    """This class will lex the provided Java source and generate a list of Function_scopes"""

    TOKEN_MATCH = re.compile("\(|\)|\{|\}|;|(\n)|\+|-|\*|/|<|>|,| ")

    def __init__(self, file_name: str) -> None:
        with open(file_name) as f:
            self.source_text = f.read()
        self.source_index = 0
        self.line_number = 1

    def lex(self) -> List[Token]:

        tokens = []

        while char := self._consume():

            if char.isspace():
                continue

            if self._handle_comments(char):
                continue

            token = self._get_token(char)
            logging.debug(f"found token \"{token}\" on line {self.line_number}")
            #tokens.append(make_token(token))

        return tokens

    def _get_token(self, char: str) -> str:
        token = char

        if not re.match(Lexer.TOKEN_MATCH, token):

            while (token_char := self._peek()):
                if re.match(Lexer.TOKEN_MATCH, token_char):
                    break
                token += self._consume()

        return token

    def _handle_comments(self, char: str) -> bool:
        if char == '/' and self._peek() == '/':
            self._get_line() #skip the entire line
            return True
        elif char == '/' and self._peek() == '*':
            self._consume()
            self._consume_until('/') #skip until closing character. Will probably bug out at some point
            return True
        return False

    def _get_line(self) -> str:
        return self._consume_until(re.compile("(\n)|;"))

    def _peek(self, offset:int = 0) -> str:
        if (self.source_index + offset) >= len(self.source_text):
            return ''
        char = self.source_text[self.source_index]
        
        return char

    def _consume(self) -> str:
        char = self._peek()

        if char == '\n':
            self.line_number += 1

        self.source_index += 1
        return char

    @overload
    def _consume_until(self, end_token: str) -> str:...

    @overload
    def _consume_until(self, end_pattern:re.Pattern) -> str:...

    def _consume_until(self, end_token) -> str:
        res = ""

        if isinstance(end_token, str):
            while self._peek() and (char:= self._consume()) != end_token:
                res += char
            
            return res

        elif isinstance(end_token, re.Pattern):
            while self._peek() and not end_token.match(char:= self._consume()):
                res += char
            
            return res