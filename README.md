# Random Sentence Generation from Grammar

In the realm of programming languages, each language encourages a unique approach to problem-solving. This project delves into the concept of polyglot programming, where utilizing multiple languages offers a broader range of capabilities. This project introduces the creation of a program that generates text based on a provided grammar.

## Core Concepts

### Grammars

A grammar comprises substitution rules dictating how symbols can be replaced with other symbols. It includes variables (symbols that can be replaced) and terminals (symbols that cannot be replaced). The grammar's rules describe a language consisting of valid text made up of terminals.

### Generating Text

The program generates text based on the specified grammar using a mutually recursive algorithm. It randomly selects options from the grammar's rules, creating sequences of terminals that form text. The process involves generating text fragments and combining them to form complete text.

## Design Requirements

- Represent the grammar using Python classes, enabling the generation of text.
- Implement a mutually recursive algorithm to generate text from the grammar.
- Utilize test doubles to improve testability, especially when dealing with input/output operations.

## Usage

To use the random text generator from a grammar, follow these steps:

1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Open this project in your preferred IDE.
4. Run the `project.py` script and follow the on-screen instructions.

## Testing

Unit tests are provided to verify the functionality of the program. These tests can be found in the `tests` directory. To run the tests, execute the appropriate test files within your IDE or via the command line.
