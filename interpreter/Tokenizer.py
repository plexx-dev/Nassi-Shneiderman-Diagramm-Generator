"""Tokenizer.py: Definition for Tokenizer class"""

import logging
import re
from typing import List, Optional

from interpreter._token import Token, make_token

class Tokenizer:
    """This class will take the provided source file and convert it to a list of tokens"""

    TOKEN_MATCH = re.compile(r"""\(|\)|\{|\}|;|(\n)|\+|-|\*|/|<|>|,| """) #TODO: make this modular

    def __init__(self, file_name: str) -> None:
        with open(file_name) as f:
            self.source_text = f.read()
        self.source_index = 0
        self.line_number = 1

        self.type_name_pattern = re.compile('(char)|(int)|(void)|(double)|(Pixel)') #TODO: make this modular

    def get_tokens(self) -> List[Token]:

        tokens = []

        while char := self._consume():

            if char.isspace():
                continue

            if self._handle_comments(char):
                continue

            token = self._get_token(char)
            logging.debug(f"found token \"{token}\" on line {self.line_number}")
            tokens.append(make_token(token, self.type_name_pattern))

        return tokens

    def _get_token(self, char: str) -> str:
        token = char

        if not re.match(Tokenizer.TOKEN_MATCH, token):

            while (token_char := self._peek()):
                if re.match(Tokenizer.TOKEN_MATCH, token_char):
                    break
                token += self._consume()

        return token

    def _handle_comments(self, char: str) -> bool:
        if char == '/' and self._peek() == '/':
            self._get_line() #skip the entire line
            return True
        elif char == '/' and self._peek() == '*':
            self._consume()
            self._consume_multiline_comment()
            return True
        return False

    def _get_line(self) -> str:
        return self._consume_until('\n')

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

    def _consume_multiline_comment(self):
        while self._peek():
            if self._consume() == '*' and self._peek() == '/':
                self._consume()
                break

    def _consume_until(self, end_tag: str) -> str:
        res = ""
        while self._peek() and (char:= self._consume()) != end_tag:
            res += char
        
        return res