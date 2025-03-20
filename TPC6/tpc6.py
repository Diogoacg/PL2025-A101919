import ply.lex as lex

# ----- Lexical Analysis -----

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    raise Exception(f"Illegal character '{t.value[0]}'")

# Build the lexer
lexer = lex.lex()

# ----- AST Classes -----

class Exp:
    """Base class for expressions in our AST"""
    def __init__(self, type, exp1, op=None, exp2=None):
        self.type = type
        self.exp1 = exp1
        self.op = op
        self.exp2 = exp2
    
    def eval(self):
        """Evaluate this expression"""
        if self.type == 'binop':
            if self.op == '+':
                return self.exp1.eval() + self.exp2.eval()
            elif self.op == '-':
                return self.exp1.eval() - self.exp2.eval()
            elif self.op == '*':
                return self.exp1.eval() * self.exp2.eval()
            elif self.op == '/':
                divisor = self.exp2.eval()
                if divisor == 0:
                    raise Exception("Division by zero")
                return self.exp1.eval() / divisor
        elif self.type == 'number':
            return self.exp1

# ----- Recursive Descent Parser -----

class Parser:
    def __init__(self):
        self.tokens = None
        self.current_token = None
    
    def get_next_token(self):
        """Get the next token from lexer"""
        self.current_token = next(self.tokens, None)
    
    def error(self):
        """Raise a syntax error"""
        if self.current_token:
            raise Exception(f"Syntax error at '{self.current_token.value}'")
        else:
            raise Exception("Syntax error: unexpected end of input")
    
    def eat(self, token_type):
        """Check and consume the current token"""
        if self.current_token and self.current_token.type == token_type:
            token = self.current_token
            self.get_next_token()
            return token
        else:
            self.error()
    
    def factor(self):
        """Parse a factor (number)"""
        token = self.eat('NUMBER')
        return Exp('number', token.value)
    
    def term(self):
        """Parse a term (factor followed by zero or more * or / operations)"""
        node = self.factor()
        
        while self.current_token and self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                node = Exp('binop', node, '*', self.factor())
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                node = Exp('binop', node, '/', self.factor())
        
        return node
    
    def expr(self):
        """Parse an expression (term followed by zero or more + or - operations)"""
        node = self.term()
        
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                node = Exp('binop', node, '+', self.term())
            elif token.type == 'MINUS':
                self.eat('MINUS')
                node = Exp('binop', node, '-', self.term())
        
        return node
    
    def parse(self, text):
        """Parse the input text and return an AST"""
        lexer.input(text)
        self.tokens = iter(lambda: lexer.token(), None)
        self.get_next_token()
        
        result = self.expr()
        
        if self.current_token:  # Check if all tokens were consumed
            self.error()
        
        return result

# ----- Main application logic -----

def evaluate_expression(expr):
    """Evaluate a mathematical expression and return the result."""
    try:
        parser = Parser()
        ast = parser.parse(expr)
        return ast.eval()
    except Exception as e:
        raise Exception(str(e))

def process_expressions(input_file, output_file):
    """Process expressions from input_file and write results to output_file."""
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    result = evaluate_expression(line)
                    # Format the result with one decimal place
                    formatted_result = f"{result:.1f}"
                    f_out.write(f"{formatted_result}\n")
                except Exception as e:
                    f_out.write(f"Error: {e}\n")

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    try:
        process_expressions(input_file, output_file)
        print(f"Processing complete. Results written to {output_file}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()