import logging
import re
from typing import Dict, List, Match, Tuple

from errors.custom import InterpreterException, JavaSyntaxError, ScopeNotFoundException
from draw.Iinstruction import *

logging.warning("""Because the Interpreter is still WIP, some Java language features are not supported. These include:
    *else if statements
    *for loops
Please remove these features from the source code as they will result in incorrect behaviour""")

class Function_scope(Iterable):
    def __init__(self, child_instructions: List[Iinstruction], name: str, return_type: str, args: List[str]) -> None:
        self.contents = child_instructions
        self.name = name
        self.return_type = return_type
        self.args = args

    def get_height(self) -> int:
        h = 0.0
        for inst in self.contents:
            h += inst.getblksize()
        return int(h)

    def __iter__(self):
        return self.contents.__iter__()

class JavaInterpreter:

    def __init__(self, filepath: str) -> None:
        with open(filepath) as file:
            if not file.readable():
                raise InterpreterException(f"Unable to read input file {filepath}")
            self.src = file.read()
            self.lines = [] # to be filled in later
        self._init_regex()
        self._recompile_regex()

    def reset_tags(self, additional_tags: Dict[str, List[str]]=None):
        """Reset the Interpreters internal tags to include the new tags given in {additional_tags}
        the key for comment tags is "comments"
        the key for tags that should be ignored is "ignore"
        the key for additional type tags is "types"
        """

        if additional_tags:
            if "comments" in additional_tags.keys():
                self.comment_tags.extend(additional_tags["comments"])
            if "ignore" in additional_tags.keys():
                self.remove_tags.extend(additional_tags["ignore"])
            if "types" in additional_tags.keys():
                self.type_tags.extend(additional_tags["types"])
                self.function_tags.extend(additional_tags["types"])
        else:
            self._init_regex()
        self._recompile_regex()

    def _init_regex(self):
        """Initialize all tag lists to their default state"""

        self.comment_tags = ["//", "#", "--"] #dont ask why a java interpreter supports lua and python style comments
        self.remove_tags = ['\n', "public", "private", "protected", "final"]
        self.type_tags = ["byte", "short", "int", "long", "float", "double", "boolean", "char", "String"]
        self.function_tags = ["void"]
        self.function_tags.extend(self.type_tags)

    def _recompile_regex(self):
        """recompile all regex's using the new tag lists"""
        comment_regex = r"""^("""
        for tag in self.comment_tags:
            comment_regex += fr"""{re.escape(tag)}|"""
        self.comment_pattern = re.compile(comment_regex[:-1]+").*", flags=re.MULTILINE)

        remove_regex = r"""^("""
        for tag in self.remove_tags:
            remove_regex += fr"""{re.escape(tag)}|"""
        self.remove_pattern = re.compile(remove_regex[:-1]+')', flags=re.MULTILINE)

        variable_regex = r"""^("""
        for tag in self.type_tags:
            variable_regex += fr"""{re.escape(tag)}|"""
        self.variable_pattern = re.compile(variable_regex[:-1]+")(.*=|.*;)(.*)", flags=re.MULTILINE)

        function_regex = r"""^(?P<return_type>"""
        for tag in self.function_tags:
            function_regex += fr"""{re.escape(tag)}|"""
        self.function_pattern = re.compile(function_regex[:-1]+")(?P<name>.*)[(](?P<args>.*)[)][^;]", flags=re.MULTILINE)

    def _check_src(self, idx: int, tag: str) -> bool:
        if idx >= len(self.lines):
            return False
        return tag in self.lines[idx]

    def _check_line_start(self, idx: int, tag: str) -> bool:
        if idx >= len(self.lines):
            return False
        return self.lines[idx].startswith(tag)

    def _get_scope_start_offset(self, i: int) -> int:
        if self._check_src(i, "{"):
            return 1
        elif self._check_src(i+1, "{"):      
            return 2
        raise ScopeNotFoundException("Unable to find scope start. Is the program ill-formed?")

    def _handle_while(self, line: str, idx: int):
        bracket_idx = line.rindex(')') # throws if while contruct is illformed

        instruction_txt = line[6:bracket_idx]
        brace_offset = self._get_scope_start_offset(idx)
        child_instructions, idx = self._get_instructions_in_scope(idx+brace_offset)
        return while_instruction_front(("while" + instruction_txt), child_instructions), idx
    
    def _handle_else(self, idx: int):
        brace_offset = self._get_scope_start_offset(idx)
        return self._get_instructions_in_scope(idx+brace_offset)

    def _get_else_scope(self, idx:int):
        instructions = None
        if self._check_line_start(idx, "}else"):
            logging.debug("found else construct in line: %i", idx+1)
            instructions, idx = self._handle_else(idx)
        
        elif self._check_line_start(idx+1, "else"):
            logging.debug("found else construct in line: %i", idx+2)
            instructions, idx = self._handle_else(idx+1)
        return instructions
        

    def _handle_if(self, line: str, idx: int):
        bracket_idx = line.rindex(')') # throws if the contruct is illformed
        instruction_txt = line[3:bracket_idx]

        brace_offset = self._get_scope_start_offset(idx)
        true_instructions, idx = self._get_instructions_in_scope(idx+brace_offset)

        false_instructions = self._get_else_scope(idx)
        
        return if_instruction(instruction_txt, true_instructions, false_instructions), idx

    def _handle_do_while(self, line: str, idx: int):
        brace_offset = self._get_scope_start_offset(idx)
        child_instructions, idx = self._get_instructions_in_scope(idx+brace_offset)

        instruction_txt = None
        if self._check_line_start(idx, "}while("):
            end_line = self.lines[idx]
            bracket_index = end_line.rindex(')') #throws if contruct id ill-formed
            instruction_txt = end_line[7:bracket_index]
        elif self._check_line_start(idx+1, "while("):
            idx += 1
            end_line = self.lines[idx]
            bracket_index = end_line.rindex(')')
            instruction_txt = end_line[6:bracket_index]
        else:
            raise JavaSyntaxError("Ill-formed do-while construct!")

        return while_instruction_back(instruction_txt, child_instructions), idx

    def _handle_variable(self, line: str, idx: int):
        groups = self.variable_pattern.match(line).groups()
        var_type = groups[0]
        var_name = groups[1][:-1]
        var_value = groups[2]
        if var_value == '':
            return generic_instruction(f"declare variable '{var_name}' of type {var_type}"), idx
        return generic_instruction(f"declare variable '{var_name}' of type {var_type} with value {var_value}"), idx

    def _handle_instruction(self, line: str, idx:int) -> Tuple[Iinstruction, int]:
        if line.startswith("while("):
            logging.debug("Found while construct in line: %i", idx+1)
            return self._handle_while(line, idx)
        
        elif line.startswith("if("):
            logging.debug("Found if construct in line: %i", idx+1)
            return self._handle_if(line, idx)

        elif line.startswith("do"):
            logging.debug("Found do-while construct in line: %i", idx+1)
            return self._handle_do_while(line, idx)

        elif self.variable_pattern.match(line):
            logging.debug("Found variable in line %i", idx+1)
            return self._handle_variable(line, idx)

        else:
            logging.debug("Found generic instruction in line %i", idx+1)
            return generic_instruction(line), idx

    def _get_instructions_in_scope(self, idx: int=0) -> Tuple[List[Iinstruction], int]:
        scope: List[Iinstruction] = []
        i = idx
        while i < len(self.lines):
            line = self.lines[i]
            
            if self._check_src(i, '}'):
                break

            instruction, i = self._handle_instruction(line, i)
            scope.append(instruction)

            i += 1
        return scope, i
    
    def _remove_keywords(self):
        self.src = self.src.replace(' ', '')
        self.src = self.comment_pattern.sub('', self.src)
        self.src = self.remove_pattern.sub('', self.src)
        self.lines = self.src.splitlines()

    def _get_function_info(self, match: Match[str]) -> Tuple[str, str, List[str]]:
        groups = match.groupdict()
        ftype = groups["return_type"]
        fargs = groups["args"]
        fname = groups["name"]
        return ftype, fname, fargs.split(',')

    def _get_function_instructions(self, function_header: str) -> List[Iinstruction]:
        idx = self.lines.index(function_header)
        brace_offset = self._get_scope_start_offset(idx)
        return self._get_instructions_in_scope(idx+brace_offset)[0]

    def _get_function_scopes(self) -> List[Function_scope]:
        scopes = []
        for match in self.function_pattern.finditer(self.src):
            span = match.span()
            header = self.src[span[0]:span[1]].replace('\n', '')

            rtype, name, args = self._get_function_info(match)

            child_instructions = self._get_function_instructions(header)

            scopes.append(Function_scope(child_instructions, name, rtype, args))
        return scopes


    def load_instruction_scopes(self):
        self._remove_keywords()
        return self._get_function_scopes()

        
# COMMENT_PATTERN = re.compile(r"""^(//|#|--)""")
# REMOVE_KEYWORDS = [' ', "public", "private", "final", "protected"]
# VARIABLE_TAGS = ["byte", "short", "int", "long", "float", "double", "boolean", "char", "String"]
# FUNCTION_IDENTIFIERS = ["void"]
# FUNCTION_IDENTIFIERS.extend(VARIABLE_TAGS)

# WHILE_TAG = "solange " #german for 'while'. Change this depending on your language

# REPLACE = dict((re.escape(k), '') for k in REMOVE_KEYWORDS)
# remove_pattern = re.compile("|".join(REPLACE.keys()), flags=re.MULTILINE)

# variable_regex = "^("
# for kw in VARIABLE_TAGS:
#     variable_regex += fr"""{kw}|"""
# variable_pattern = re.compile(variable_regex[0:-1]+")(.*=|.*;)(.*)", flags=re.MULTILINE)

# function_regex = "^(?P<return_type>"
# for kw in FUNCTION_IDENTIFIERS:
#     function_regex += fr"""{kw}|"""
# function_regex = function_regex[0:-1]+ ")(?P<name>.*)[(](?P<args>.*)[)][^;]"

# function_pattern = re.compile(function_regex, flags=re.MULTILINE)

# def check_src(src: List[str], line_index: int, tag: str) -> bool:
#     if line_index >= len(src):
#         return False
#     return tag in src[line_index]

# def check_line_start(src: List[str], line_index: int, tag: str) -> bool:
#     if line_index >= len(src):
#         return False
#     return src[line_index].startswith(tag)

# def get_next_occurence_of(src: List[str], start_idx:int, tag:str) -> int:
#     """Returns the index of the next occurence of tag in src from start_idx"""
#     i = start_idx
#     while i < len(src):
#         if check_src(src, i, tag):
#             break
#         i += 1
#     return i

# def get_scope_start_offset(src: List[str], i: int) -> int:
#     if check_src(src, i, "{"):
#         return 1
#     elif check_src(src, i+1, "{"):
#         return 2
#     raise ScopeNotFoundException("Unable to find scope start. Is the program ill-formed?")


# def get_function_scopes(src: str) -> List[Function_scope]:
#     scopes = []
#     lines = src.splitlines(True)
#     for match in function_pattern.finditer(src):

#         span = match.span()
#         matched_str = src[span[0]:span[1]]

#         rtype, name, args = get_function_info(match, matched_str)

#         child_instructions = get_function_instructions(lines, matched_str)

#         scopes.append(Function_scope(child_instructions, name, rtype, args))
#     return scopes