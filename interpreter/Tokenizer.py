"""Tokenizer.py: Definition for Tokenizer class"""

from errors.custom import JavaSyntaxError
import logging
import re
from typing import List, Optional

from interpreter._token import Token, make_token, SourceLocation

class Tokenizer:
    """This class will take the provided source file and convert it to a list of tokens"""

    TOKEN_MATCH = re.compile(r"""\(|\)|\{|\}|;|(\n)|\+|-|\*|/|<|>|,| """)

    def __init__(self, file_name: str) -> None:
        with open(file_name) as f:
            self.source_text = f.read()
        self.source_index = 0
        self.line_number = 1
        self.column_number = 0

        self.source_text = re.sub("(private)|(public)|(protected)|(final)", "", self.source_text)

        self.type_name_pattern = re.compile('(char)|(int)|(void)|(double)|(boolean)|(Pixel)|(String)') #TODO: make this modular

        self._filename = file_name

        self._left_curly_number=0
        self._right_curly_number=0

    def get_tokens(self) -> List[Token]:

        tokens = []

        while char := self._consume():

            if char.isspace():
                continue

            if self._handle_comments(char):
                continue

            tag = self._get_token(char)
            logging.debug(f"found tag \"{tag}\" on line {self.line_number}")

            if tag == "{":
                self._left_curly_number+=1
            elif tag == "}":
                self._right_curly_number+=1

            tokens.append(make_token(tag, SourceLocation(self._filename, self.line_number, self.column_number), self.type_name_pattern))

        if self._left_curly_number != self._right_curly_number:
            raise JavaSyntaxError(f"Ill-formed Java program! Expected equal number of '{'{'}' and '{'}'}' tokens, got {self._left_curly_number} and {self._right_curly_number}")

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
            self.column_number = 1

        self.source_index += 1
        self.column_number += 1
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