import re

# Define the language syntax
KEYWORDS = ['if', 'else', 'while', 'print']
TOKEN_REGEX = re.compile(r'\b\w+\b|\+|\-|\*|\/|\(|\)')

# Tokenize the input
def tokenize(input_string):
    tokens = TOKEN_REGEX.findall(input_string)
    tokens = [token if token not in KEYWORDS else 'KEYWORD' for token in tokens]
    return tokens

# Parse the tokens
def parse(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == 'KEYWORD':
            if tokens[i+1] == '(':
                print(f'{tokens[i]} statement')
                i += 2
                continue
            else:
                print(f'{tokens[i]} keyword')
        else:
            print(f'Operator: {tokens[i]}')
        i += 1

# Evaluate the input
def evaluate(input_string):
    tokens = tokenize(input_string)
    parse(tokens)

input_string = 'if (x > y) print(x)'
evaluate(input_string)
