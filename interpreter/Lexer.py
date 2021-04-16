"""Lexer.py: Definition for Lexer class"""
from interpreter.Tokenizer import Tokenizer
from os import linesep
from draw.Iinstruction import *
from typing import List, Optional, Union, Tuple
import logging

from interpreter.function_scope import Function_scope
from interpreter._token import Token, Token_type
from errors.custom import JavaSyntaxError

def print_arr(arr):
    print("[")
    for elem in arr:
        if isinstance(elem, List):
            print_arr(elem)
        else:
            print(elem)
    print("]")

class Lexer:
    def __init__(self, tokens: List[Token]) -> None:
        self._tokens = tokens
        self._token_index = 0

        self._scopes: List[Function_scope] = []

        #in case the tokenizer finds valid tokens in the global scope, they will be saved here
        self._global_instructions = []

    

    def _peek(self, offset:int=0) -> Optional[Token]:
        if (self._token_index+offset) >= len(self._tokens):
            return None
        return self._tokens[self._token_index+offset]

    def _consume(self):
        token = self._peek()
        self._token_index+=1
        return token


    def get_instructions(self):

        scopes = []

        while self._peek():
            line_tokens = self.get_line_tokens()

            if self._is_function_def(line_tokens):

                func_name, func_return_type, func_args = self._construct_function_header_from_tokens(line_tokens)
                current_scope = Function_scope(func_name, func_return_type, func_args)

                instructions = self._get_instructions_in_scope()
                current_scope._add_instructions(instructions)

                scopes.append(current_scope)

            else:
                #something was declared in global scope
                self._global_instructions.append(self._construct_instruction_from_tokens(line_tokens))

        self.add_globals_to_scope_list(scopes)
        return scopes
            
    def _get_instructions_in_scope(self):

        instructions = []

        while self._peek():

            line_tokens = self.get_line_tokens()
            instruction = self._construct_instruction_from_tokens(line_tokens)
            if instruction:
                instructions.append(instruction)

            delimiter_token = line_tokens[-1]
            if delimiter_token.type == Token_type.RIGHT_CURLY:
                return instructions

        raise JavaSyntaxError(f"{self._peek(-1).location}: Missing right curly!")



    def get_tokens_until(self, delimiter_types: List[Token_type]) -> List[Token]:
        tokens = []
        while token := self._consume():
            tokens.append(token)
            if token.type in delimiter_types:
                break
        return tokens

    def get_line_tokens(self):
        return self.get_tokens_until([Token_type.SEMICOLON, Token_type.LEFT_CURLY, Token_type.RIGHT_CURLY])

    

    def add_globals_to_scope_list(self, scope_list: List[Function_scope]):
        global_scope = Function_scope("<Global scope>", "void", [])
        global_scope._add_instructions(self._global_instructions)

        scope_list.append(global_scope)


    def _is_function_def(self, tokens: List[Token]) -> bool:
        #if token list is of shape TYPE_NAME IDENTIFIER ( ... {
        return tokens[0].type == Token_type.TYPE_NAME and tokens[1].type == Token_type.UNKNOWN and tokens[2].type == Token_type.LEFT_PAREN and tokens[-1].type == Token_type.LEFT_CURLY



    def _construct_instruction_from_tokens(self, tokens: List[Token]):
        instruction_token = tokens[0]

        if instruction_token.type == Token_type.IF_STATEMENT:
            return self._handle_if_construct(tokens)
        
        elif instruction_token.type == Token_type.WHILE_STATEMENT:
            return self._handle_while_construct(tokens)
            
        elif instruction_token.type == Token_type.DO_WHILE_STATEMENT:
            return self._handle_do_while_construct(tokens)
        
        elif instruction_token.type == Token_type.FOR_STATEMENT:
            return self._handle_for_construct(tokens)
        
        elif instruction_token.type == Token_type.TYPE_NAME:
            return self._handle_type_name_construct(tokens)

        elif instruction_token.type == Token_type.UNKNOWN:
            return self._handle_generic_construct(tokens)

    def _construct_function_header_from_tokens(self, tokens: List[Token]) -> Tuple[str, str, List[str]]:

        _ensure_correct_function_structure(tokens)

        function_return_type = tokens[0].content

        function_name = tokens[1].content

        argument_list = _get_function_argument_list_from_tokens(tokens[3:-2])

        return function_name, function_return_type, argument_list

    def _construct_variable_def_from_tokens(self, tokens: List[Token]) -> str:
        _ensure_correct_variable_structure(tokens)

        variable_type = tokens[0].content
        variable_name = tokens[1].content

        if tokens[2].type == Token_type.SEMICOLON:
            return f"declare variable '{variable_name}' of type {variable_type}"

        variable_value = self._construct_source_line_from_tokens(tokens[3:])

        return f"declare variable '{variable_name}' of type {variable_type} with value {variable_value}"

    def _construct_source_line_from_tokens(self, tokens: List[Token]) -> str:
        """TODO: make this function smarter"""
        line = ""

        for token in tokens:
            if token.type == Token_type.SEMICOLON:
                break
            line += token.content + ' '

        return line[:-1] #ignore the space after the last instruction text

    """Handler functions for different types of language structures"""

    def _handle_if_construct(self, tokens: List[Token]):
        logging.debug("Found if construct")

        _ensure_correct_if_structure(tokens)

        condition_str = self._construct_source_line_from_tokens(tokens[2:-2])

        true_case = self._get_instructions_in_scope()
        false_case = self._handle_else_construct()

        return if_instruction(condition_str, true_case, false_case)

    def _handle_else_construct(self):
        if self._peek().type == Token_type.ELSE_STATEMENT:
            if self._peek(1).type == Token_type.IF_STATEMENT:
                logging.debug("Found if-else construct")
                else_if_tokens = self.get_line_tokens()[1:]
                return [self._handle_if_construct(else_if_tokens)]
            else:
                logging.debug("Found else construct")
                self.get_line_tokens()
                return self._get_instructions_in_scope()
        return None

    def _handle_while_construct(self, tokens: List[Token]):
        logging.debug("Found while construct")

        _ensure_correct_while_structure(tokens)

        condtion_str = self._construct_source_line_from_tokens(tokens[2:-2])
        
        loop_instructions = self._get_instructions_in_scope()

        return while_instruction_front(condtion_str, loop_instructions)

    def _handle_do_while_construct(self, tokens: List[Token]):
        logging.debug("Found do-while construct")

        _ensure_correct_do_while_structure_part_1(tokens)


        loop_instructions = self._get_instructions_in_scope()


        while_tokens = self.get_line_tokens()
        _ensure_correct_do_while_structure_part_2(while_tokens)
        condtion_str = self._construct_source_line_from_tokens(while_tokens[2:-2])

        return while_instruction_back(condtion_str, loop_instructions)

    def _handle_for_construct(self, tokens: List[Token]):
        logging.debug("Found for construct")
        tokens.extend(self.get_tokens_until([Token_type.LEFT_CURLY]))

        _ensure_correct_for_structure(tokens)

        variable_tokens, condition_tokens, increment_tokens = _get_for_arguments_from_tokens(tokens[2:])
        
        variable_str = ""
        if len(variable_tokens) > 1: #if we got more than just a semicolon
            variable_str = self._construct_variable_def_from_tokens(variable_tokens)

        condition_str = "true"
        if condition_tokens:
            condition_str = self._construct_source_line_from_tokens(condition_tokens)

        increment_instruction = None
        if increment_tokens:
            increment_instruction = generic_instruction(self._construct_source_line_from_tokens(increment_tokens))

        loop_instructions = self._get_instructions_in_scope()

        if increment_instruction:
            loop_instructions.append(increment_instruction)

        return for_instruction(variable_str, condition_str, loop_instructions)

    def _handle_type_name_construct(self, tokens: List[Token]):
        logging.debug("Found Type name construct")
        
        return generic_instruction(self._construct_variable_def_from_tokens(tokens))

    def _handle_generic_construct(self, tokens: List[Token]):
        logging.debug("Found generic instruction")

        return generic_instruction(self._construct_source_line_from_tokens(tokens))



def _ensure_correct_function_structure(tokens: List[Token]):
    #function structure: TYPE_NAME IDENTIFIER ( ... ) {
    if len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed function declaration! Expected at least 5 tokens, got {len(tokens)}")
    if tokens[-1].type != Token_type.LEFT_CURLY:
        raise JavaSyntaxError(f"{tokens[-1].location}: Ill-formed function declaration! Expected last token to be LEFT_CURLY, got {str(tokens[-1].type)}")
    if tokens[1].type != Token_type.UNKNOWN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after function return type! Expected UNKNWON, got {str(tokens[1].type)}")
    if tokens[2].type != Token_type.LEFT_PAREN:
        raise JavaSyntaxError(f"{tokens[2].location}: Illegal token after funtion name! Expected LEFT_CURLY, got {str(tokens[2].type)}")
    if tokens[-2].type != Token_type.RIGTH_PAREN:
        raise JavaSyntaxError(f"{tokens[-2].location}: Illegal token after function parameter list! Expected RIGHT_PAREN, got {str(tokens[-2].type)}")

def _ensure_correct_variable_structure(tokens: List[Token]):
    #variable structure: TYPE_NAME IDENTIFIER ;|( = EXPRESSION;)
    if len(tokens) < 3:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed type construct! Expected at least 3 tokens, got {len(tokens)}")
    if tokens[1].type != Token_type.UNKNOWN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after type name! Expected UNKNOWN, got {str(tokens[1].type)}")
    if not tokens[2].type in [Token_type.SEMICOLON, Token_type.EQUAL_SIGN]:
        raise JavaSyntaxError(f"{tokens[2].location}: Illegal token after variable name! Expected SEMICOLON or EQUAL_SIGN, got {str(tokens[2].type)}")
    if tokens[2].type == Token_type.EQUAL_SIGN and len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[2].location}: Ill-formed assignment expression! Expected at least 5 tokens, got {len(tokens)}")

def _ensure_correct_if_structure(tokens: List[Token]):
    #if structure: IF ( ... ) {  <-- the opening curly is technically not needed, but we require it anyways
    if len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed if construct! Expected at least 5 tokens, got {len(tokens)}")
    if tokens[-1].type != Token_type.LEFT_CURLY:
        raise JavaSyntaxError(f"{tokens[-1].location}: Ill-formed if construct! Expected last token to be LEFT_CURLY, got {str(tokens[-1].type)}")
    if tokens[1].type != Token_type.LEFT_PAREN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after if token! Expected LEFT_PAREN, got {str(tokens[1].type)}")
    if tokens[-2].type != Token_type.RIGTH_PAREN:
        raise JavaSyntaxError(f"{tokens[-2].location}: Illegal token after conditional expression! Expected RIGHT_PAREN, got {str(tokens[-2].type)}")

def _ensure_correct_while_structure(tokens: List[Token]):
    #while structure: WHILE ( ... ) { <-- might not be required by the standard, but is required by us
    if len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed while construct! Expected at least 5 tokens, got {len(tokens)}")
    if tokens[-1].type != Token_type.LEFT_CURLY:
        raise JavaSyntaxError(f"{tokens[-1].location}: Ill-formed while construct! Expected last token to be LEFT_CURLY, got {str(tokens[-1].type)}")
    if tokens[1].type != Token_type.LEFT_PAREN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after while token! Expected LEFT_PAREN, got {str(tokens[1].type)}")
    if tokens[-2].type != Token_type.RIGTH_PAREN:
        raise JavaSyntaxError(f"{tokens[-2].location}: Illegal token after while condition! Expected RIGHT_PAREN, got {str(tokens[-2].type)}")

def _ensure_correct_do_while_structure_part_1(tokens: List[Token]):
    #do-while structure: do{
    if len(tokens) != 2:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed do-while construct! Expected 2 tokens, got {len(tokens)}")
    if tokens[1].type != Token_type.LEFT_CURLY:
        raise JavaSyntaxError(f"Illegal token after do token! Expected LEFT_CURLY, got {str(tokens[1].type)}")

def _ensure_correct_do_while_structure_part_2(tokens: List[Token]):
    #do-while structure: while( ... );
    if len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed do while contruct! Expected at least 5 tokens, got {len(tokens)}")
    if tokens[0].type != Token_type.WHILE_STATEMENT:
        raise JavaSyntaxError(f"{tokens[0].location}: Illegal token after do block! Expected WHILE_STATEMENT, got {str(tokens[1].type)}")
    if tokens[-1].type != Token_type.SEMICOLON:
        raise JavaSyntaxError(f"{tokens[-1].location}: Ill-formed do-while construct! Expected last token to be SEMICOLON, got {str(tokens[-1].type)}")
    if tokens[1].type != Token_type.LEFT_PAREN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after while token! Expected LEFT_PAREN, got {str(tokens[1].type)}")
    if tokens[-2].type != Token_type.RIGTH_PAREN:
        raise JavaSyntaxError(f"{tokens[-2].location}: Illegal token after do-while condition! Expected RIGHT_PAREN, got {str(tokens[-2].type)}")

def _ensure_correct_for_structure(tokens: List[Token]):
    #for structure: for(...?;...?;...?) {
    if len(tokens) < 6:
        raise JavaSyntaxError(f"{tokens[0].location}: Illf-formed for loop construct! Expected at least 6 tokens, got {len(tokens)}")
    if tokens[-1].type != Token_type.LEFT_CURLY:
        raise JavaSyntaxError(f"{tokens[-1].location}: Ill-formed for loop construct! Expected last token to be LEFT_CURLY, got {str(tokens[-1].type)}")
    if tokens[1].type != Token_type.LEFT_PAREN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after for token! Expected LEFT_PAREN, got {str(tokens[1].type)}")
    if tokens[-2].type != Token_type.RIGTH_PAREN:
        raise JavaSyntaxError(f"{tokens[-2].location}: Illegal token after for loop increment! Expected RIGHT_PAREN, got {str(tokens[-2].type)}")
    if ( semicolon_count := tokens.count(Token(Token_type.SEMICOLON)) ) != 2:
        raise JavaSyntaxError(f"Ill-formed for loop construct! Expected exactly 2 SEMICOLON tokens, got {semicolon_count}")



def _get_function_argument_list_from_tokens(tokens: List[Token]) -> List[str]:
    arg_tokens = _get_seperated_token_list(tokens, [Token_type.COMMA])

    args = []
    
    for arg in arg_tokens:
        arg_str = ""
        for token in arg:
            arg_str += token.content + ' '
        arg_str = arg_str[:-1]
        args.append(arg_str)

    return args

def _get_seperated_token_list(tokens: List[Token], seperator_types: List[Token_type]) -> List[List[Token]]:
    token_segments = []
    tokens_in_segment = []

    for token in tokens:
        if token.type in seperator_types:
            token_segments.append(tokens_in_segment)
            tokens_in_segment = []
            continue
        tokens_in_segment.append(token)

    token_segments.append(tokens_in_segment)

    return token_segments


def _get_for_arguments_from_tokens(tokens: List[Token]) -> Tuple[List[Token], List[Token],  List[Token]]:
    variable_tokens = []
    condition_tokens = []
    increment_tokens = []

    token_index = 0

    while True:
        token = tokens[token_index]
        token_index += 1

        variable_tokens.append(token)
        if token.type == Token_type.SEMICOLON:
            break
    
    while True:
        token = tokens[token_index]
        token_index += 1

        if token.type == Token_type.SEMICOLON:
            break
        condition_tokens.append(token)

    while True:
        token = tokens[token_index]
        token_index += 1

        if token.type == Token_type.LEFT_CURLY:
            break
        increment_tokens.append(token)

    return variable_tokens, condition_tokens, increment_tokens[:-1]