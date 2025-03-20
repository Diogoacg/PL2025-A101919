import ply.lex as lex

# Lista de tokens
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
]

# Regras para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

# Regra para números (inteiros ou decimais)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Inválido: {t.value[0]}")
    t.lexer.skip(1)

# Construir o analisador léxico
lexer = lex.lex()