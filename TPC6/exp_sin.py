import ply.yacc as yacc
from exp_lex import tokens

# Ordem de operações
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

# Regras gramaticais
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ZeroDivisionError("Divisão por zero")
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro de sintaxe: '{p.value}'")
    else:
        print("Erro de sintaxe: fim inesperado da expressão")

# Construir o parser
parser = yacc.yacc()

# Função para avaliar expressões
def evaluate_expression(expression):
    try:
        return parser.parse(expression)
    except Exception as e:
        return f"Erro: {str(e)}"