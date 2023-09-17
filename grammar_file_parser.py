import tempfile

from grammar_objects import Grammar, Rule, Option, Variable, Terminal
import pathlib

class Grammar_File_Parser:
    def __init__(self):
        self._grammar = None

    def grammar(self):
        """Returns grammar object attribute"""
        return self._grammar

    def parse_grammar_file(self, grammar_file_path):
        """Main function which parses a grammar file, given a file path. It starts by opening the file, returning if the path is invalid. If valid, it opens the file and calls the
           extract_grammar method passing in the file lines as the argument. After calculating a result of the grammar obj (and there fore all other grammar objects), it assigns
           the grammar object to the class variable _grammar."""
        file_path = pathlib.Path(grammar_file_path)
        # no need to handle file path w/ out extension.

        # if invalid_path, return:
        if not pathlib.Path.is_file(file_path):
            print('PATH DOES NOT exist')
            return

        with open(file_path, 'r') as file:                  # Open grammar file


            print(file.readlines())

            grammar_obj = self.extract_grammar(file.readlines())
            self._grammar = grammar_obj


    def extract_grammar(self, file_lines):
        """Function which takes in the file lines of a grammar file. The function loops over every line and reads one at a time. If a line is equal to the '{' symbol, it means the start of a
           rule, and it calls the extract_rule function passing in the correct index and file_lines. After extracting the rule_obj, it updates the current index, skipping the lines read in the extract_rule
           function. If the lines is not equal to '{', we do nothing & continue iteration. After all lines have been read, the function creates a grammar object, passing in the rules extracted, and returns
           the Grammar object."""
        rules = []                                           # list of rule objects extracted from file.
        for i in range(len(file_lines)):                     # Loop thru all lines
            line = file_lines[i].strip()
            if line == '{':                                  # START RULE
                i += 1                                       # otherwise starts on '{'
                rule_obj = self.extract_rule(i, file_lines)  # extract rule obj.
                rules.append(rule_obj)

                # update the current line we're reading:
                lines_skipped = len(rule_obj._options) + 1   # lines we read in extract_rule_objects & thus need to skip, is equal to #rules + variable.
                i += lines_skipped                           # total lines covered (options + variable)
        # END
        grammar_obj = Grammar(rules)  # Empty grammar obj
        return grammar_obj
    
    def extract_rule(self, line_index, file_lines):
        """"Function that takes in a line index, which is set to the start of the rule, and the file_lines of the file we are reading through. It loops through each line, the first being the varaible
            associated with the rule, and the rest which are options of the rule. It creates a new variable for the single variable line, and new option objects for each line which is an option.
            The function continues until it reads a '}' symbol, signifying the end of the function, in which case it breaks. Finally it creates and returns a new rule object, passing the varaible and options with
            extracted from the lines read."""

        rule_variable = None
        rules_options = []

        for i in range(line_index, len(file_lines)):
            line = file_lines[i].strip()

            if line == '}':                                                 # END of RULE
                break
            elif i == line_index:                                           # Start Variable => Always comes after {, first line in rule.
                rule_variable = Variable(line)
            else:                                                           # OPTION: weight, symbols
                new_option = self.extract_option(line)

                if new_option:
                    rules_options.append(new_option)

        # Create new RULE OBJECT: variable, options
        new_rule = Rule(rule_variable, rules_options)
        return new_rule

    def extract_option(self, line):
        """"Function which takes in a single line from a grammar file, which consists of data for an option. The first item in this line will always be the weight of the option, and
            the rest will be the symbols. We loop through each symbol and determine if its a variable or terminal. If the symbol start with a '[' and ends with a ']', we know its a variable, and
            create a variable object, passing the contents of the brackets as its argument. Otherwise we create a terminal object, and we just pass the symbol as its argument. We add these objects
            to a list called symbols. After looping through each symbol, we create a new option object, which takes in the symbols we extracted, and the weight, and we return it"""
        line = line.split()
        weight = int(line[0])  # first in line
        symbols_lines = line[1:]  # rest of line
        symbols = []

        if weight == 0:
            return None

        # break symbol line into terminals & variables
        for symbol in symbols_lines:
            try:
                start_bracket = symbol[0]
                end_bracket = symbol[-1]
                if start_bracket == '[' and end_bracket == ']':         # Extract Variable
                    symbol = symbol.replace('[','')
                    symbol = symbol.replace(']','')
                    if symbol != '':                                    # If not empty brackets
                        new_variable = Variable(symbol)
                        symbols.append(new_variable)
                else:
                    raise ValueError                                    # if doesn't meet [] conditions, must be a terminal (raise error to call exception)
            except:
                new_terminal = Terminal(symbol)
                symbols.append(new_terminal)

        new_option = Option(weight, symbols)
        return new_option

    # def debug_grammar_objects(self):
    #     print('grammar rules:', len(self._grammar.rules()))
    #     print('variable rule dict:', self._grammar.variable_rule_dict())
    #
    #     for rule in self._grammar.rules():
    #         print('RULE:')
    #         print(rule.variable().text())
    #         for option in rule.options():
    #             symbs_text = [f'{type(s).__name__}:"{s.text()}"' for s in option.symbols()]
    #             print(option.weight(), symbs_text)


# TEST DOUBLE CLASS
class Grammar_File_Parser_Double:
    def __init__(self):
        self._grammar = None

    def grammar(self):
        """Returns grammar object attribute"""
        return self._grammar

    def parse_grammar_file(self, file_lines):
        """Main function which parses a grammar file, given a file path. It starts by opening the file, returning if the path is invalid. If valid, it opens the file and calls the
           extract_grammar method passing in the file lines as the argument. After calculating a result of the grammar obj (and there fore all other grammar objects), it assigns
           the grammar object to the class variable _grammar."""

        grammar_obj = self.extract_grammar(file_lines)
        self._grammar = grammar_obj

    def extract_grammar(self, file_lines):
        """Function which takes in the file lines of a grammar file. The function loops over every line and reads one at a time. If a line is equal to the '{' symbol, it means the start of a
           rule, and it calls the extract_rule function passing in the correct index and file_lines. After extracting the rule_obj, it updates the current index, skipping the lines read in the extract_rule
           function. If the lines is not equal to '{', we do nothing & continue iteration. After all lines have been read, the function creates a grammar object, passing in the rules extracted, and returns
           the Grammar object."""
        rules = []  # list of rule objects extracted from file.
        for i in range(len(file_lines)):  # Loop thru all lines
            line = file_lines[i].strip()
            if line == '{':  # START RULE
                i += 1  # otherwise starts on '{'
                rule_obj = self.extract_rule(i, file_lines)  # extract rule obj.
                rules.append(rule_obj)

                # update the current line we're reading:
                lines_skipped = len(
                    rule_obj._options) + 1  # lines we read in extract_rule_objects & thus need to skip, is equal to #rules + variable.
                i += lines_skipped  # total lines covered (options + variable)
        # END
        grammar_obj = Grammar(rules)  # Empty grammar obj
        return grammar_obj

    def extract_rule(self, line_index, file_lines):
        """"Function that takes in a line index, which is set to the start of the rule, and the file_lines of the file we are reading through. It loops through each line, the first being the varaible
            associated with the rule, and the rest which are options of the rule. It creates a new variable for the single variable line, and new option objects for each line which is an option.
            The function continues until it reads a '}' symbol, signifying the end of the function, in which case it breaks. Finally it creates and returns a new rule object, passing the varaible and options with
            extracted from the lines read."""

        rule_variable = None
        rules_options = []

        for i in range(line_index, len(file_lines)):
            line = file_lines[i].strip()

            if line == '}':  # END of RULE
                break
            elif i == line_index:  # Start Variable => Always comes after {, first line in rule.
                rule_variable = Variable(line)
            else:  # OPTION: weight, symbols
                new_option = self.extract_option(line)

                if new_option:
                    rules_options.append(new_option)

        # Create new RULE OBJECT: variable, options
        new_rule = Rule(rule_variable, rules_options)
        return new_rule

    def extract_option(self, line):
        """"Function which takes in a single line from a grammar file, which consists of data for an option. The first item in this line will always be the weight of the option, and
            the rest will be the symbols. We loop through each symbol and determine if its a variable or terminal. If the symbol start with a '[' and ends with a ']', we know its a variable, and
            create a variable object, passing the contents of the brackets as its argument. Otherwise we create a terminal object, and we just pass the symbol as its argument. We add these objects
            to a list called symbols. After looping through each symbol, we create a new option object, which takes in the symbols we extracted, and the weight, and we return it"""
        line = line.split()
        weight = int(line[0])  # first in line
        symbols_lines = line[1:]  # rest of line
        symbols = []

        if weight == 0:
            return None

        # break symbol line into terminals & variables
        for symbol in symbols_lines:
            try:
                start_bracket = symbol[0]
                end_bracket = symbol[-1]
                if start_bracket == '[' and end_bracket == ']':  # Extract Variable
                    symbol = symbol.replace('[', '')
                    symbol = symbol.replace(']', '')
                    if symbol != '':  # If not empty brackets
                        new_variable = Variable(symbol)
                        symbols.append(new_variable)
                else:
                    raise ValueError  # if doesn't meet [] conditions, must be a terminal (raise error to call exception)
            except:
                new_terminal = Terminal(symbol)
                symbols.append(new_terminal)

        new_option = Option(weight, symbols)
        return new_option