import logging
import re
from typing import Dict, List, Match, Tuple, Union

from errors.custom import InterpreterException, JavaSyntaxError, ScopeNotFoundException
from draw.Iinstruction import *

logging.warning("""Because the Interpreter is still WIP, some Java language features are not supported. These include:
    *foreach loops (will throw JavaSyntaxError)
    *constructors (will be ignored)
    *switch statements
    *Generics
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
            h += inst.getblkheight()
        return int(h)

    def get_width(self) -> int:
        w = 200.0
        for inst in self.contents:
            w = max(w, inst.getblkwidth())
        return int(w)

    def __iter__(self):
        return self.contents.__iter__()

class JavaInterpreter:

    def __init__(self, filepath: str) -> None:
        with open(filepath) as file:
            if not file.readable():
                raise InterpreterException(f"Unable to read input file {filepath}")
            self._src = file.read() #WARNING: throws if file is too large
            self._lines = [] # to be filled in later
        self.reset_tags()

    def reset_tags(self, additional_tags: Dict[str, List[str]]=None):
        """Reset the Interpreters internal tags to include the new tags given in {additional_tags} or default.
        The key for comment tags is "comments"
        The key for tags that should be ignored is "ignore"
        The key for additional type tags is "types"
        """

        if additional_tags:
            if "comments" in additional_tags.keys():
                tags = additional_tags["comments"]
                if tags:
                    self._comment_tags.extend(tags)
            if "ignore" in additional_tags.keys():
                tags = additional_tags["ignore"]
                if tags:
                    self._remove_tags.extend(tags)
            if "types" in additional_tags.keys():
                tags = additional_tags["types"]
                if tags:
                    self._type_tags.extend(tags)
                    self._function_tags.extend(tags)
        else:
            self._init_regex()
        self._recompile_regex()

    def load_instruction_scopes(self):
        self._remove_keywords()
        return self._get_function_scopes()

    def _init_regex(self):
        """Initialize all tag lists to their default state"""

        self._comment_tags = ["//", "#", "--"] #dont ask why a java interpreter supports lua and python style comments
        self._remove_tags = ['\n', "public", "private", "protected", "final"]
        self._type_tags = ["byte", "short", "int", "long", "float", "double", "boolean", "char", "String"]
        self._function_tags = ["void"]
        self._function_tags.extend(self._type_tags)

    def _recompile_regex(self):
        """recompile all regex's using the new tag lists"""
        comment_regex = r"""^("""
        for tag in self._comment_tags:
            comment_regex += fr"""{re.escape(tag)}|"""
        self._comment_pattern = re.compile(comment_regex[:-1]+").*", flags=re.MULTILINE)

        remove_regex = r"""^("""
        for tag in self._remove_tags:
            remove_regex+= fr"""{re.escape(tag)}|"""
        self._remove_pattern = re.compile(remove_regex[:-1]+')', flags=re.MULTILINE)

        variable_regex = r"""^("""
        for tag in self._type_tags:
            variable_regex += fr"""{re.escape(tag)}|"""
        self._variable_pattern = re.compile(variable_regex[:-1]+")(.*=|.*;)(.*)", flags=re.MULTILINE)

        function_regex = r"""^(?P<return_type>"""
        for tag in self._function_tags:
            function_regex += fr"""{re.escape(tag)}|"""
        self._function_pattern = re.compile(function_regex[:-1]+")(?P<name>.*)[(](?P<args>.*)[)][^;]", flags=re.MULTILINE)

    def _check_src(self, idx: int, tag: str) -> bool:
        if idx >= len(self._lines):
            return False
        return tag in self._lines[idx]

    def _check_line_start(self, idx: int, tag: str) -> bool:
        if idx >= len(self._lines):
            return False
        return self._lines[idx].startswith(tag)

    def _get_scope_start_offset(self, i: int) -> int:
        if self._check_src(i, "{"):
            return 1
        elif self._check_src(i+1, "{"):
            return 2
        raise ScopeNotFoundException("Unable to find scope start. Is the program ill-formed?")

    def _get_subscope(self, idx: int):
        brace_offset = self._get_scope_start_offset(idx)
        return self._get_instructions_in_scope(idx+brace_offset)

    def _handle_while(self, line: str, idx: int):
        bracket_idx = line.rindex(')') # throws if while contruct is illformed

        instruction_txt = line[6:bracket_idx]
        child_instructions, idx = self._get_subscope(idx)
        return while_instruction_front(("while" + instruction_txt), child_instructions), idx

    def _get_else_scope(self, idx:int):
        instructions = None
        if self._check_line_start(idx, "}else"):
            if self._check_src(idx, "if("):
                logging.debug("found else if construct in line: %i", idx+1)
                line = self._lines[idx][5:]
                instructions, idx = self._handle_if(line, idx)
                instructions = [instructions]
            else:
                logging.debug("found else construct in line: %i", idx+1)
                instructions, idx = self._get_subscope(idx)

        elif self._check_line_start(idx+1, "else"):
            if self._check_src(idx+1, "if("):
                logging.debug("found else if construct in line: %i", idx+2)
                line = self._lines[idx+1][4:]
                instructions, idx = self._handle_if(line, idx+1)
                instructions = [instructions]
            else:
                logging.debug("found else construct in line: %i", idx+2)
                instructions, idx = self._get_subscope(idx+1)
        return instructions, idx


    def _handle_if(self, line: str, idx: int):
        bracket_idx = line.rindex(')') # throws if the contruct is illformed
        instruction_txt = line[3:bracket_idx]

        true_instructions, idx = self._get_subscope(idx)

        false_instructions, idx = self._get_else_scope(idx)

        return if_instruction(instruction_txt, true_instructions, false_instructions), idx

    def _handle_do_while(self, line: str, idx: int):
        brace_offset = self._get_scope_start_offset(idx)
        child_instructions, idx = self._get_instructions_in_scope(idx+brace_offset)

        instruction_txt = None
        if self._check_line_start(idx, "}while("):
            end_line = self._lines[idx]
            bracket_index = end_line.rindex(')') #throws if contruct id ill-formed
            instruction_txt = end_line[7:bracket_index]
        elif self._check_line_start(idx+1, "while("):
            idx += 1
            end_line = self._lines[idx]
            bracket_index = end_line.rindex(')')
            instruction_txt = end_line[6:bracket_index]
        else:
            raise JavaSyntaxError("Ill-formed do-while construct!")

        return while_instruction_back(instruction_txt, child_instructions), idx

    def _handle_for(self, line: str, idx: int):
        #line: for(type|name;condition;increment)
        segments = line.split(";")
        try:
            var = segments[0][4:]
            cond = segments[1]
            inc = segments[2][:-2]

            instructions = []

            if cond == "": #did you know test expressions where optional and defaulted to true? Me neither
                cond = "true"

            if var != "":
                variable_instruction = self._handle_variable(var, idx)[0]
                instructions.append(variable_instruction)

            brace_offset =  self._get_scope_start_offset(idx)
            child_instructions, idx = self._get_instructions_in_scope(idx+brace_offset)

            if inc != "":
                increment_instruction = generic_instruction(inc)
                child_instructions.append(increment_instruction)

            instructions.append(for_instruction("while " + cond, child_instructions))

            return instructions, idx

        except IndexError:
            raise JavaSyntaxError("Ill-formed for loop construct!")
        except:
            raise

    def _handle_variable(self, line: str, idx: int):
        groups = self._variable_pattern.match(line).groups()
        var_type = groups[0]
        var_name = groups[1][:-1]
        var_value = groups[2]
        if var_value == '':
            return generic_instruction(f"declare variable '{var_name}' of type {var_type}"), idx
        return generic_instruction(f"declare variable '{var_name}' of type {var_type} with value {var_value}"), idx

    def _handle_instruction(self, line: str, idx:int) -> Tuple[Union[Iinstruction, List[Iinstruction]], int]:
        if line.startswith("while("):
            logging.debug("Found while construct in line: %i", idx+1)
            return self._handle_while(line, idx)

        elif line.startswith("if("):
            logging.debug("Found if construct in line: %i", idx+1)
            return self._handle_if(line, idx)

        elif line.startswith("do"):
            logging.debug("Found do-while construct in line: %i", idx+1)
            return self._handle_do_while(line, idx)

        elif line.startswith("for("):
            logging.debug("Found for construct in line: %i", idx+1)
            return self._handle_for(line, idx)

        elif self._variable_pattern.match(line):
            logging.debug("Found variable in line %i", idx+1)
            return self._handle_variable(line, idx)

        else:
            logging.debug("Found generic instruction in line %i", idx+1)
            return generic_instruction(line), idx

    def _get_instructions_in_scope(self, idx: int=0) -> Tuple[List[Iinstruction], int]:
        scope: List[Iinstruction] = []
        i = idx
        while i < len(self._lines):
            line = self._lines[i]

            if self._check_src(i, '}'):
                break

            instruction, i = self._handle_instruction(line, i)
            if isinstance(instruction, List):
                scope.extend(instruction)
            else:
                scope.append(instruction)

            i += 1
        return scope, i

    def _remove_keywords(self):
        self.src = self._src.replace(' ', '')
        self.src = self._comment_pattern.sub('', self.src)
        self.src = self._remove_pattern.sub('', self.src)
        self._lines = self.src.splitlines()

    def _get_function_info(self, match: Match[str]) -> Tuple[str, str, List[str]]:
        groups = match.groupdict()
        ftype = groups["return_type"]
        fargs = groups["args"].split(',')
        fname = groups["name"]
        return ftype, fname, fargs

    def _get_function_instructions(self, function_header: str) -> List[Iinstruction]:
        idx = self._lines.index(function_header)
        brace_offset = self._get_scope_start_offset(idx)
        return self._get_instructions_in_scope(idx+brace_offset)[0]

    def _get_function_scope(self, match: Match[str]):
        span = match.span()
        header = self.src[span[0]:span[1]].replace('\n', '')

        rtype, name, args = self._get_function_info(match)

        child_instructions = self._get_function_instructions(header)

        return Function_scope(child_instructions, name, rtype, args)

    def _get_function_scopes(self) -> List[Function_scope]:
        matches = self._function_pattern.finditer(self.src)
        return list(map(self._get_function_scope, matches))