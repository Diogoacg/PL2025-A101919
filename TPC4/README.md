# Analisador Léxico para SPARQL

**Data:** 6 de março de 2025

# Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

# Resumo

Este programa implementa um analisador léxico (lexer) para consultas SPARQL, utilizando a biblioteca PLY (Python Lex-Yacc). O analisador identifica e classifica diferentes componentes das consultas SPARQL, como palavras-chave, identificadores, literais, números e símbolos especiais.

## Algoritmo

O algoritmo utiliza a biblioteca PLY para definir e reconhecer tokens numa consulta SPARQL. As principais etapas do algoritmo são:

1. **Definição de tokens**: Definem-se os tokens que serão reconhecidos pelo analisador léxico, como `SELECT`, `WHERE`, `LIMIT`, identificadores, literais, etc.
2. **Definição de regras lexicais**: Para cada tipo de token, é definida uma expressão regular que descreve o padrão a reconhecer.
3. **Processamento de tokens especiais**: Alguns tokens requerem tratamento adicional, como a conversão de números em inteiros.
4. **Tratamento de elementos ignoráveis**: São definidas regras para ignorar comentários e espaços em branco.
5. **Tratamento de erros**: É implementada uma função para lidar com caracteres não reconhecidos.
6. **Construção e execução do analisador**: O analisador léxico é construído e recebe uma consulta de exemplo para análise.

## Expressões Regulares Utilizadas

- **Identificadores**: `\?[a-zA-Z_][a-zA-Z0-9_]*` - Reconhece variáveis que começam com `?` seguidas por letras, números e sublinhados.
- **Literais**: `"[^"]+"(@[a-zA-Z]+)?` - Reconhece cadeias de caracteres entre aspas duplas, possivelmente seguidas por uma etiqueta de idioma.
- **Palavras**: `[a-zA-Z][a-zA-Z0-9]*:[a-zA-Z][a-zA-Z0-9]*|[a-zA-Z][a-zA-Z0-9]*` - Reconhece palavras simples ou termos com prefixos (ex: `foaf:name`).
- **Números**: `\d+` - Reconhece sequências de dígitos.
- **Comentários**: `\#.*` - Reconhece linhas que começam com `#` e ignora-as.

## Exemplo de Uso

```bash
cd TPC4
python tpc4.py
```

### Se Plylex não estiver instalado

```bash
pip install ply
```

### Exemplo de query SPARQL

```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

### Saída

```bash
LexToken(SELECT,'select',3,33)
LexToken(IDENTIFIER,'?nome',3,40)
LexToken(IDENTIFIER,'?desc',3,46)
LexToken(WHERE,'where',3,52)
LexToken(LBRACE,'{',3,58)
LexToken(IDENTIFIER,'?s',4,60)
LexToken(A,'a',4,63)
LexToken(WORD,'dbo:MusicalArtist',4,65)
LexToken(DOT,'.',4,82)
LexToken(IDENTIFIER,'?s',5,84)
LexToken(WORD,'foaf:name',5,87)
LexToken(LITERAL,'"Chuck Berry"@en',5,97)
LexToken(DOT,'.',5,114)
LexToken(IDENTIFIER,'?w',6,116)
LexToken(WORD,'dbo:artist',6,119)
LexToken(IDENTIFIER,'?s',6,130)
LexToken(DOT,'.',6,132)
LexToken(IDENTIFIER,'?w',7,134)
LexToken(WORD,'foaf:name',7,137)
LexToken(IDENTIFIER,'?nome',7,147)
LexToken(DOT,'.',7,152)
LexToken(IDENTIFIER,'?w',8,154)
LexToken(WORD,'dbo:abstract',8,157)
LexToken(IDENTIFIER,'?desc',8,170)
LexToken(RBRACE,'}',9,176)
LexToken(LIMIT,'LIMIT',9,178)
LexToken(NUMBER,1000,9,184)
```

# Lista de Resultados
[Código Python](tpc4.py)