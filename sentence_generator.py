import random
from grammar_objects import Grammar, Rule, Option, Variable, Terminal

class Random_Sentence_Generator:
    # DUCK TYPING
    # GENERATOR
    # MUTUALLY RECURSIVE

    def __init__(self, grammar_obj):
        self._grammar_obj = grammar_obj

    def generate_random_sentence(self, start_variable_text, num_sentences):
        """Function which takes in a start variable string, and an int of number of sentences to generate.
           It runs a loop for num_sentences, and in each loop, creates a new variable object start variable form the passed variable_text.
           It then yields the result from the frag_from_variable function."""
        for i in range(num_sentences):
            start_variable = Variable(start_variable_text)
            yield next(self.frag_from_variable(start_variable)).rstrip()


    def frag_from_variable(self, variable):
        """"Takes in a variable object, and gets reference to a rule object from the passed variable, with the _variable_rule_dict dictionary.
            This function then returns the result of frag_from_rule with the rule object passed."""
        # Find rule from start variable:
        variable_rule_dict = self._grammar_obj.variable_rule_dict()
        rule = variable_rule_dict[variable.text()]

        # ask rule to generate fragment:
        yield next(self.frag_from_rule(rule))

    def frag_from_rule(self, rule):
        """"Function which takes in rule object and gets a random option from that rule object using the random_option_in_rule function. This function
            returns the result of passing the random option into the random_option_in_rule function."""
        # choose random option
        rand_option = self.random_option_in_rule(rule)

        #ask option to generate fragment:
        yield next(self.frag_from_option(rand_option))

    def frag_from_option(self, option):
        """"Function which takes in an option object, and loops over each symbol in the passed option's symbols. For each symbol we check if it is a Terminal
            or Variable object. If it is a Terminal, we add the Terminal text to a str called sentence. If the symbol is a variable, we pass it to frag_from_variable,
            and then add the result from that function call to sentence. After looping over every symbol and adding the value to sentence, we return the string sentence."""
        # iterate thru symbols, generate fragments from each symbol.
        sentence = ''

        for symb in option.symbols():
            # terminal:
            if type(symb) is Terminal:
                sentence += f'{symb.text()} '

            # variable:
            elif type(symb) is Variable:
                # find corresponding rule, repeat process..
                value = next(self.frag_from_variable(symb))   # should eventually return string terminal.
                sentence += f'{value}'

        yield sentence

    def random_option_in_rule(self, rule):
        """Selects random option from available options given a provided rule. It does this by adding instances of options based on the number of their weight,
           then selecting a random option of the total option list. Finally it returns this random option object."""
        options = rule.options()

        # corresponding weight & option will watch by index between the two lists.
        weights = []
        for option in options:
            weights.append(option.weight())

        # for i in range(len(options)):
        #     print('weight:', weights[i], 'option:', [s.text() for s in options[i].symbols()])

        rand_option = random.choices(options, weights = weights, k = 1)[0]
        #print('rand_option', [f'{type(s).__name__}:"{s.text()}"' for s in rand_option.symbols()])

        return rand_option


class Sentence_Generator_Double:
    # DUCK TYPING
    # GENERATOR
    # MUTUALLY RECURSIVE

    def __init__(self, grammar_obj):
        self._grammar_obj = grammar_obj

    def generate_sentence(self, start_variable_text, num_sentences):
        """Function which takes in a start variable string, and an int of number of sentences to generate.
           It runs a loop for num_sentences, and in each loop, creates a new variable object start variable form the passed variable_text.
           It then yields the result from the frag_from_variable function."""
        for i in range(num_sentences):
            start_variable = Variable(start_variable_text)
            yield next(self.frag_from_variable(start_variable)).rstrip()

    def frag_from_variable(self, variable):
        """"Takes in a variable object, and gets reference to a rule object from the passed variable, with the _variable_rule_dict dictionary.
            This function then returns the result of frag_from_rule with the rule object passed."""
        # Find rule from start variable:
        variable_rule_dict = self._grammar_obj.variable_rule_dict()
        rule = variable_rule_dict[variable.text()]

        # ask rule to generate fragment:
        yield next(self.frag_from_rule(rule))

    def frag_from_rule(self, rule):
        """"Function which takes in rule object and gets a random option from that rule object using the random_option_in_rule function. This function
            returns the result of passing the random option into the random_option_in_rule function."""

        # RANDOM PART: could just pick first option, or pass in an option as parameter...
        rand_option = rule.options()[0]
        #rand_option = self.random_option_in_rule(rule)

        #ask option to generate fragment:
        yield next(self.frag_from_option(rand_option))

    def frag_from_option(self, option):
        """"Function which takes in an option object, and loops over each symbol in the passed option's symbols. For each symbol we check if it is a Terminal
            or Variable object. If it is a Terminal, we add the Terminal text to a str called sentence. If the symbol is a variable, we pass it to frag_from_variable,
            and then add the result from that function call to sentence. After looping over every symbol and adding the value to sentence, we return the string sentence."""
        # iterate thru symbols, generate fragments from each symbol.
        sentence = ''


        for symb in option.symbols():
            # terminal:
            if type(symb) is Terminal:
                sentence += f'{symb.text()} '

            # variable:
            elif type(symb) is Variable:
                # find corresponding rule, repeat process..
                value = next(self.frag_from_variable(symb))   # should eventually return string terminal.
                sentence += f'{value}'

        yield sentence

    def random_option_in_rule(self, rule):
        """Selects random option from available options given a provided rule. It does this by adding instances of options based on the number of their weight,
           then selecting a random option of the total option list. Finally it returns this random option object."""
        options = rule.options()

        # corresponding weight & option will watch by index between the two lists.
        weights = []
        for option in options:
            weights.append(option.weight())

        # for i in range(len(options)):
        #     print('weight:', weights[i], 'option:', [s.text() for s in options[i].symbols()])

        rand_option = random.choices(options, weights = weights, k = 1)[0]
        #print('rand_option', [f'{type(s).__name__}:"{s.text()}"' for s in rand_option.symbols()])

        return rand_option



