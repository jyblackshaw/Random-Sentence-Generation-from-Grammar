import unittest
from grammar_file_parser import Grammar_File_Parser_Double
from grammar_objects import Grammar, Rule, Option, Variable, Terminal


class TestGrammarFileParser(unittest.TestCase):

    file_lines = ['{\n',
                  'HowIsBoo\n',
                  '1 Boo is [Adjective] today\n',
                  '1 Boo is [Adjective] today\n',
                  '}\n',
                  '\n',
                  '{\n',
                  'Adjective\n',
                  '3 happy\n',
                  '3 perfect\n',
                  '}\n',
                  '\n',
                  '{\n',
                  'Verb\n',
                  '2 run\n',
                  '2 jump\n',
                  '0 sleep\n',
                  '}\n']

    def test_parse_grammar_file(self):
        grammar_parser = Grammar_File_Parser_Double()
        grammar_parser.parse_grammar_file(self.file_lines)
        grammar_obj = grammar_parser.grammar()


        # NOTE: Remember, all asserts are reference to the GrammarFileParserDouble, hardcoded input!!
        self.assertTrue(type(grammar_obj) is Grammar)

        # Test grammar's rules:
        grammar_rules = grammar_obj.rules()
        self.assertEqual(len(grammar_rules), 3) # assert length

        # Test Grammar Obj variable_dict:
        variable_rule_dict = grammar_obj.variable_rule_dict()
        key_pairs = [(r.variable().text(), r) for r in grammar_rules]

        # make sure key_pairs in variable_rule_dict are accurate.
        for pair in key_pairs:
            var_text = pair[0]
            rule = pair[1]

            self.assertTrue(var_text in variable_rule_dict)
            self.assertTrue(variable_rule_dict[var_text] == rule)

    def test_extract_option(self):
        grammar_parser = Grammar_File_Parser_Double()
        grammar_parser.parse_grammar_file(self.file_lines)
        grammar_obj = grammar_parser.grammar()
        nested_options = [r.options() for r in grammar_obj.rules()]
        options = sum(nested_options, [])

        # Test option weight & symbols:
        self.assertEqual(len(options), 6)

        # 0 weight option:
        zero_weight_option = f'0 happy\n'
        self.assertEqual(grammar_parser.extract_option(zero_weight_option), None)

class TestGrammarObjects(unittest.TestCase):
    def test_option_object(self):
        symbols = [Terminal('Boo'), Terminal('is'), Variable('happy'), Terminal('today')]
        option = Option(1, symbols)

        self.assertEqual(option.weight(), 1)
        self.assertEqual(option.symbols(), symbols)

    # Other objects don't seem to need coverage

class TestSentenceGenerator(unittest.TestCase):
    pass

class TestProject4(unittest.TestCase):
    pass
