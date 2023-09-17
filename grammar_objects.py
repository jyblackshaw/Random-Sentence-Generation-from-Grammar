class Grammar:
    def __init__(self, rules):
        self._rules = rules                                            # list of rule objects
        self._variable_rule_dict = self.create_variable_rule_dict()    # variable_name (str) : corresponding rule obj

    def rules(self):
        """returns attribute _rules"""
        return self._rules

    def variable_rule_dict(self):
        """returns attribute _variable_rule_dict"""
        return self._variable_rule_dict

    def create_variable_rule_dict(self):
        """Function which loops through each rule from self._rules. It creates a new dictionary, and for each rule it gets reference to the variable & its name, and sets a reference
           from the variable_name as key, and rule object as value, in this new dictionary. Finally, it returns the new dictionary which is to be set in the __init__ method, to the _variable_rule_dict
           attribute."""

        variable_rules_dict = {}
        for rule in self._rules:
            variable_name = rule.variable().text()
            variable_rules_dict[variable_name] = rule

        return variable_rules_dict

class Rule:
    def __init__(self, variable, options):
        self._variable = variable  # variable object associated w/ rule.
        self._options = options    # list of option objects

    def variable(self):
        """returns attribute _variable"""
        return self._variable

    def options(self):
        """returns attribute _options"""
        return self._options

class Option:
    def __init__(self, weight, symbols):
        self._weight = weight    # int
        self._symbols = symbols  # Statement is made of terminals & variable objs.. just ordered list? # Does not include weight

    def weight(self):
        """returns attribute _weight"""
        return self._weight

    def symbols(self):
        """returns attribute _symbols"""
        return self._symbols

class Variable:
    def __init__(self, text):
        self._text = text
    def text(self):
        """returns attribute _name"""
        return self._text



class Terminal:
    def __init__(self, text):
        self._text = text

    def text(self):
        """returns attribute _text"""
        return self._text