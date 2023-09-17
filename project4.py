# project4.py
#
# ICS 33 Winter 2023
# Project 4: Still Looking for Something
from grammar_file_parser import Grammar_File_Parser
from sentence_generator import Random_Sentence_Generator
from grammar_objects import Variable

def main() -> None:
    #grammar_file_path = raw_input()  # if only file_name, assume cwd. (project directory).
    # Assume its valid, ie. don't need to test for invalid grammar files or paths.
    # Don't need to test for infinite grammars.

    # DEBUG:

    num_sentences = 5 # int > 0, number of random sentences to generate.
    start_variable_text_1 = 'HowIsBoo'  # JUST name of start variable.
    start_variable_text_2 = 'GrinStatement'  # JUST name of start variable.


    #path inputs:
    debug_path = f'C:\\Users\\jybla\\PycharmProjects\\Project4_winter\\grin.txt'
    debug_file_name = f'grin.txt'
    debug_file_name2 = f'grammar.txt'

    g_file_converter = Grammar_File_Parser()
    g_file_converter.parse_grammar_file(debug_file_name2)
    grammar_obj = g_file_converter.grammar()

    rand_sentence_generator = Random_Sentence_Generator(grammar_obj)
    rand_sentences = rand_sentence_generator.generate_random_sentence('HowIsBoo', 5)

    for i in range(5):
        print(next(rand_sentences))


#REAL

    # grammar_file = input()
    # num_sentences = int(input())  # int > 0, number of random sentences to generate.
    # start_variable_text = input()  # JUST name of start variable.
    #
    # g_file_converter = Grammar_File_Converter()
    # g_file_converter.Grammar_File_To_Objects(grammar_file)
    # grammar_obj = g_file_converter.grammar()
    #
    # rand_sentence_generator = Random_Sentence_Generator(grammar_obj)
    # rand_sentences = rand_sentence_generator.generate_random_sentence(start_variable_text, num_sentences)

    # Sanity checker returning #'s??


    # for i in range(num_sentences):
    #     print(next(rand_sentences))



if __name__ == '__main__':
    main()
