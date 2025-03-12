# Máquina de Vendas Automática

**Data:** 12 de março de 2025

# Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

# Resumo

Este programa implementa uma máquina de vendas automática que permite listar produtos, inserir moedas, selecionar produtos, adicionar novos produtos ao stock e devolver troco. O programa utiliza a biblioteca PLY (Python Lex-Yacc) para análise léxica dos comandos.

## Algoritmo

O algoritmo utiliza a biblioteca PLY para definir e reconhecer tokens nos comandos da máquina de vendas. As principais etapas do algoritmo são:

1. **Definição de tokens**: Definem-se os tokens que serão reconhecidos pelo analisador léxico, como `LISTAR`, `MOEDA`, `SELECIONAR`, `ADICIONAR`, `SAIR`, `AJUDA`, `COD`, `NOME`, `QUANTIDADE`, `UNIDADE`, `PRECO`, `EURO`, `CENT`.
2. **Definição de regras lexicais**: Para cada tipo de token, é definida uma expressão regular que descreve o padrão a reconhecer.
3. **Processamento de tokens especiais**: Alguns tokens requerem tratamento adicional, como a conversão de números em inteiros ou floats.
4. **Tratamento de elementos ignoráveis**: São definidas regras para ignorar espaços em branco e vírgulas.
5. **Tratamento de erros**: É implementada uma função para lidar com caracteres não reconhecidos.
6. **Construção e execução do analisador**: O analisador léxico é construído e recebe comandos de exemplo para análise.

## Expressões Regulares Utilizadas

- **Código**: `[A-Za-z]\d+` - Reconhece códigos que começam com uma letra seguida por dígitos.
- **Nome**: `"[^"]+"` - Reconhece cadeias de caracteres entre aspas duplas.
- **Euros**: `[0-9]+[eE]` - Reconhece valores em euros.
- **Cêntimos**: `[0-9]+[cC]` - Reconhece valores em cêntimos.
- **Quantidade**: `(?<!\.)\b\d+\b(?!\.)` - Reconhece quantidades inteiras.
- **Preço**: `\d+\.\d+` - Reconhece preços em formato decimal.
- **Unidade**: `[a-zA-Z]+` - Reconhece unidades de medida.

## Exemplo de Uso

```bash
cd TPC5
python tpc5.py
```

### Se Plylex não estiver instalado

```bash
pip install ply
```

### Comandos Disponíveis

- **LISTAR**: Mostra os produtos disponíveis.
- **MOEDA <valores>**: Insere moedas (ex: 1e, 50c, 20c).
- **SELECIONAR <código>**: Seleciona um produto pelo código.
- **ADICIONAR <código> "<nome>" <quantidade> [<unidade>] <preço>**: Adiciona um produto ao stock.
- **SAIR**: Sai do sistema e devolve o troco.
- **AJUDA**: Mostra a mensagem de ajuda.

### Exemplo de Comandos

```bash
>> LISTAR
maq:
cod   | nome                 | quantidade | preço
--------------------------------------------------
A23   | Água 0.5L            | 7          | 0.7  
B45   | Coca-Cola 0.33L      | 5          | 1.2  
C67   | Pringles 40g         | 10         | 1.0  
D89   | M&M's 50g            | 3          | 1.5  
E12   | Oreo 66g             | 7          | 2.0  
A21   | KitKat 41.5g         | 9          | 0.75 
B43   | Snickers 50g         | 6          | 1.0  
C65   | Twix 50g             | 4          | 1.0  
D87   | Bounty 57g           | 2          | 1.25 
E10   | Mars 51g             | 8          | 1.0  
A22   | Bolachas 100g        | 4          | 0.75 

>> MOEDA 1e 50c
maq: Saldo = 1e50c

>> SELECIONAR A23
maq: Pode retirar o produto dispensado "Água 0.5L"
maq: Saldo = 80c

>> ADICIONAR B46 "Pepsi 0.33L" 10 1.1
maq: Novo produto "Pepsi 0.33L" adicionado ao stock.

>> SAIR
maq: Pode retirar o troco: 80c.
maq: Até à próxima
```

# Lista de Resultados
[Código Python](tpc5.py)
[Stock Json](stock.json)