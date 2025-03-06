import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'A',
    'WORD',          # Para palavras normais como "name", "artist", etc.
    'NUMBER',        # Para números como em "LIMIT 1000"
    'IDENTIFIER',    # Variáveis que começam com ?
    'LITERAL',       # Strings entre aspas
    'LBRACE',
    'RBRACE',
    'DOT',
    'COLON',
    'AT',
)

# Expressões regulares para tokens simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COLON = r':'
t_AT = r'@'

# Expressões regulares mais complexas

def t_SELECT(t):
    r'select'
    return t

def t_WHERE(t):
    r'where'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t

def t_A(t):
    r'a'
    return t

def t_IDENTIFIER(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LITERAL(t):
    r'"[^"]+"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_WORD(t):
    r'[a-zA-Z][a-zA-Z0-9]*:[a-zA-Z][a-zA-Z0-9]*|[a-zA-Z][a-zA-Z0-9]*'
    return t

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

# Ignorar comentários (linhas começando com #)
def t_COMMENT(t):
    r'\#.*'
    pass  # Comentários são ignorados

# Controlo de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Testar o lexer com uma query de exemplo
data = """
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

# Alimentar o lexer com a entrada
lexer.input(data)

# Tokenizar a entrada
while True:
    tok = lexer.token()
    if not tok:
        break  # Fim da entrada
    print(tok)