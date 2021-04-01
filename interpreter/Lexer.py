"""Lexer.py: Definition for Lexer class"""
from interpreter.Tokenizer import Tokenizer
from os import linesep
from draw.Iinstruction import *
from typing import List, Optional, Union, Tuple
import logging

from interpreter.function_scope import Function_scope
from interpreter._token import Token, Token_type
from errors.custom import JavaSyntaxError
class Lexer:
    def __init__(self, tokens: List[Token]) -> None:
        self._tokens = tokens
        self._token_index = 0

        self._scopes: List[Function_scope] = []
        self._current_scope = None

        self._current_scoped_instruction = None

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
                fs = Function_scope(func_name, func_return_type, func_args)

                instructions = self._get_instructions_in_scope()
                fs._add_instructions(instructions)

                scopes.append(fs)

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

        raise JavaSyntaxError(f"Missing right curly!")



    def get_line_tokens(self):
        tokens = []
        while token := self._consume():
            tokens.append(token)
            if token.type in [Token_type.SEMICOLON, Token_type.LEFT_CURLY, Token_type.RIGHT_CURLY]:
                break
        return tokens

    

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
        return "name", "return_type", ["int arg1", "String arg2"]

    def _construct_variable_def_from_tokens(self, tokens: List[Token]) -> str:
        #token_list: TYPE_NAME IDENTIFIER ;|( = EXPRESSION)
        _ensure_correct_variable_structure(tokens)
        if var_value:
            return f"decalare variable '{'name'}' of type {'type'} type with value {'value'}"
        return f"declare variable '{'name'}' of type {'type'}"

    """Handler functions for different types of language structures"""

    def _handle_if_construct(self, tokens: List[Token]):
        logging.debug("Found if construct")

        true_case = self._get_instructions_in_scope()
        false_case = self._handle_else_construct()

        return if_instruction("if_instruction", true_case, false_case)

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
        
        loop_instructions = self._get_instructions_in_scope()

        return while_instruction_front("while_instruction", loop_instructions)

    def _handle_do_while_construct(self, tokens: List[Token]):
        logging.debug("Found do-while construct")

        loop_instructions = self._get_instructions_in_scope()

        self.get_line_tokens()

        return while_instruction_back("while_instruction_back", loop_instructions)



    def _handle_for_construct(self, tokens: List[Token]):
        #TODO: change that
        logging.debug("Found for construct")
        tokens.extend(self.get_line_tokens())
        tokens.extend(self.get_line_tokens())

        loop_instructions = self._get_instructions_in_scope()

        loop_instructions.append(generic_instruction("increment"))

        return for_instruction("for_instruction", loop_instructions)

    def _handle_type_name_construct(self, tokens: List[Token]):
        logging.debug("Found Type name construct")
        _ensure_correct_variable_structure(tokens)
        return generic_instruction("type_name_construct")

    def _handle_generic_construct(self, tokens: List[Token]):
        logging.debug("Found generic instruction")

        return generic_instruction("generic_instruction")

def _ensure_correct_variable_structure(tokens: List[Token]):
    #variable structure: TYPE_NAME IDENTIFIER ;|( = EXPRESSION)
    if len(tokens) < 3:
        raise JavaSyntaxError(f"{tokens[0].location}: Ill-formed type construct! Expected at least 3 tokens, got {len(tokens)}")
    if tokens[1].type != Token_type.UNKNOWN:
        raise JavaSyntaxError(f"{tokens[1].location}: Illegal token after type name! Expected UNKNOWN, got {str(tokens[1].type)}")
    if not tokens[2].type in [Token_type.SEMICOLON, Token_type.EQUAL_SIGN]:
        raise JavaSyntaxError(f"{tokens[2].location}: Illegal token after variable name! Expected SEMICOLON or EQUAL_SIGN, got {str(tokens[2].type)}")
    if tokens[2].type == Token_type.EQUAL_SIGN and len(tokens) < 5:
        raise JavaSyntaxError(f"{tokens[2].location}: Ill-formed assignment expression! Expected at least 5 tokens, got {len(tokens)}")

#     def get_scopes(self) -> List[Function_scope]:

#         while token := self._consume_token():

#             if token.type == Token_type.IF_STATEMENT:
#                 self._handle_if_construct()

#             elif token.type == Token_type.WHILE_STATEMENT:
#                 self._handle_while_construct()
            
#             elif token.type == Token_type.FOR_STATEMENT:
#                 self._handle_for_construct()
#             elif token.type == Token_type.DO_WHILE_STATEMENT:
#                 self._handle_do_while_construct()

#             elif token.type == Token_type.TYPE_NAME:
#                 self._handle_type_identifier(token)

#             elif token.type == Token_type.UNKNOWN:
#                 self._handle_unknown_token(token)
        
#         self._handle_globals()
#         return self._scopes

#     def _append_scoped_instructions_to_parent(self, parent_instruction: Iinstruction):
#         indent_depth = 1
#         past_instructions = []
#         current_parent_instruction = parent_instruction
#         while (token := self._consume_token()) and indent_depth > 0:

#             current_instruction = self.get_instruction_from_token(token)

#             if token.type == Token_type.RIGHT_CURLY:
#                 current_parent_instruction = past_instructions.pop()
#                 indent_depth-=1

#             if token.type == Token_type.LEFT_CURLY:
#                 past_instructions.append(current_instruction)
#                 current_parent_instruction = 


#     def _handle_if_construct(self):
#         self._check_construct("Illformed if construct!")

#         logging.debug("found if construct")
#         if_tokens = self._get_argument_tokens()
        
#         if_text = _construct_source_line_from_tokens(if_tokens)

#         self.add_instruction_to_active_scope(if_instruction(if_text, [], []))

#     def _handle_while_construct(self):
#         self._check_construct("Illformed while construct!")

#         logging.debug("Found while construct")
#         while_tokens = self._get_argument_tokens()
        
#         while_text = _construct_source_line_from_tokens(while_tokens)

#         self.add_instruction_to_active_scope(while_instruction_front(while_text, []))

#     def _handle_for_construct(self):
#         self._check_construct("Illformed for construct!")

#         logging.debug("Found for construct")
#         for_tokens = self._get_argument_tokens()

#         variable_inst, condition_str, increment_inst = _construct_for_arguments_from_tokens(for_tokens)

#         self.add_instruction_to_active_scope(variable_inst)
#         self.add_instruction_to_active_scope(for_instruction(condition_str, []))

#     def _handle_do_while_construct(self):
#         if self._consume_token().type != Token_type.LEFT_CURLY:
#             raise JavaSyntaxError("Illformed do-while construct!")
        
#         logging.debug("Found do-while contruct")

#         #These are the instructions in the loops scope
#         do_while_tokens = self._consume_tokens_until(Token_type.WHILE_STATEMENT) #this will break, but what is the best way to do this? Stack evaluation?
        
#         while_argument_tokens = self._get_argument_tokens();
#         while_argument_string = _construct_source_line_from_tokens(while_argument_tokens)

#         self.add_instruction_to_active_scope(while_instruction_back(while_argument_string, []))

#     def _handle_type_identifier(self, token: Token):
#         if self._token_is_function_def():
#             logging.debug("Function definition found")
#             self._handle_new_function_def(token)

#         elif self._token_is_var_dec():
#             logging.debug("Variable declaration found")
#             self.add_instruction_to_active_scope(self._make_var_dec(token))

#         elif self._token_is_var_def():
#             logging.debug(f"Variable definition found")
#             self.add_instruction_to_active_scope(self._make_var_def(token))

#         else:
#             raise JavaSyntaxError("Illegal token after type identifier!")

#     def _handle_unknown_token(self, token: Token):
#         logging.debug("Found unknown Token. Most likely function call")
#         self.add_instruction_to_active_scope(self._make_generic_instruction(token))



#     def _token_is_function_def(self) -> bool:
#         return self._peek_token().type == Token_type.UNKNOWN and self._peek_token(1).type == Token_type.LEFT_PAREN
    
#     def _token_is_var_dec(self) -> bool:
#         return self._peek_token().type == Token_type.UNKNOWN and self._peek_token(1).type == Token_type.SEMICOLON
    
#     def _token_is_var_def(self) -> bool:
#         return self._peek_token().type == Token_type.UNKNOWN and self._peek_token(1).type == Token_type.EQUAL_SIGN



#     def _make_var_dec(self, token) -> generic_instruction:
#         var_type = token.content
#         var_name = self._consume_token().content
#         return _construct_generic_instruction_from_variable_def(var_type, var_name, "")

#     def _make_var_def(self, token) -> generic_instruction:
#         var_type = token.content
#         var_name = self._consume_token().content
#         line_tokens = self._get_tokens_until_semicolon()

#         var_value_str = _construct_source_line_from_tokens(line_tokens)

#         return _construct_generic_instruction_from_variable_def(var_type, var_name, var_value_str)

#     def _make_generic_instruction(self, token: Token) -> Iinstruction:
#         line_tokens = self._get_tokens_until_semicolon()
#         line_tokens.insert(0, token)
#         line_text = _construct_source_line_from_tokens(line_tokens)

#         return generic_instruction(line_text)

#     def _handle_new_function_def(self, token: Token):
#         function_return_type = token.content
#         function_name = self._consume_token().content
#         self._consume_token() #get rid of the left parenthesis
        
#         argument_tokens = self._get_argument_tokens()

#         arg_list = _construct_arg_list_from_tokens(argument_tokens)

#         self._add_scope(function_name, function_return_type, arg_list)


#     def add_instruction_to_active_scope(self, instruction: Union[Iinstruction, List[Iinstruction]]):
#         if isinstance(instruction, List):
#             if self._current_scope:
#                 self._current_scope.contents.extend(instruction)
#             else:
#                 self._global_instructions.extend(instruction)
#         else:
#             if self._current_scope:
#                 self._current_scope._add_instruction(instruction)
#             else:
#                 self._global_instructions.append(instruction)



#     def _add_scope(self, function_name: str, function_return_type: str, function_args: List[str]):
#         if self._current_scope:
#             self._scopes.append(self._current_scope) #do not append the global scope as it is still in use
#         self._current_scope = Function_scope(function_name, function_return_type, function_args) #add a new empty function scope to the list of scopes


#     def _handle_globals(self):
#         """Append all globally declared instructions, if any, to the list of all scopes"""
#         if len(self._global_instructions) > 0:
#             global_scope = Function_scope("<Global>", "", [])
#             global_scope._add_instructions(self._global_instructions)



#     def _check_construct(self, msg:str):
#         if self._consume_token().type != Token_type.LEFT_PAREN:
#             raise JavaSyntaxError(msg)


#     def _get_tokens_until_semicolon(self) -> List[Token]:
#         return self._consume_tokens_until(Token_type.SEMICOLON)

#     def _get_argument_tokens(self) -> List[Token]:
#         return self._consume_tokens_until(Token_type.RIGTH_PAREN)

#     def _consume_tokens_until(self, end_type: Token_type) -> List[Token]:
#         tokens = []
#         while self._peek_token() and (token := self._consume_token()).type != end_type:
#             tokens.append(token)
#         return tokens

# def _construct_generic_instruction_from_variable_def(var_type:str, var_name: str, var_value: str) -> generic_instruction:
#     if var_value:
#         return generic_instruction(f"declare variable '{var_name}' of type '{var_type}' with value {var_value}")
#     return generic_instruction(f"declare variable '{var_name}' of type '{var_type}'")

# def _construct_source_line_from_tokens(tokens: List[Token]) -> str:
#     return "src" #TODO: implement

# def _construct_arg_list_from_tokens(token: List[Token]) -> List[str]:
#     return ["arg"] #TODO: implement

# def _construct_for_arguments_from_tokens(tokens: List[Token]) -> Tuple[str, str, str]:
#     return generic_instruction("var"), "con", "inc" #TODO: implement