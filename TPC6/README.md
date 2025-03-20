# Calculadora de Expressões Matemáticas

**Data:** 20 de março de 2025

# Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

# Resumo

Este programa implementa uma calculadora de expressões matemáticas que processa um arquivo de entrada contendo expressões matemáticas e gera um arquivo de saída com os resultados dos cálculos. O programa utiliza a biblioteca PLY (Python Lex-Yacc) para análise léxica e um parser recursivo descendente para a análise sintática das expressões.

## Algoritmo

O algoritmo utiliza a biblioteca PLY para definir e reconhecer tokens nas expressões matemáticas. As principais etapas do algoritmo são:

1. **Análise Léxica**:
   - Definição dos tokens: `NUMBER`, `PLUS`, `MINUS`, `MULTIPLY`, `DIVIDE`.
   - Definição de expressões regulares para cada tipo de token.
   - Processamento de números com suporte para decimais.
   - Tratamento de espaços em branco e erros léxicos.

2. **Modelação da AST (Abstract Syntax Tree)**:
   - Implementação da classe `Exp` para representar expressões.
   - Suporte para expressões numéricas e operações binárias.
   - Método de avaliação (`eval`) para calcular o resultado das expressões.

3. **Análise Sintática (Parser)**:
   - Implementação de um parser recursivo descendente.
   - Funções específicas para cada nível de precedência: `expr`, `term`, e `factor`.
   - Suporte para precedência de operadores (multiplicação e divisão antes de adição e subtração).
   - Detecção de erros sintáticos.

4. **Processamento de Arquivos**:
   - Leitura de expressões de um arquivo de entrada.
   - Avaliação de cada expressão utilizando o parser e a AST.
   - Formatação dos resultados com uma casa decimal.
   - Escrita dos resultados em um arquivo de saída.

## Expressões Regulares Utilizadas

- **Número**: `\d+(\.\d+)?` - Reconhece números inteiros ou decimais.
- **Adição**: `\+` - Reconhece o operador de adição.
- **Subtração**: `-` - Reconhece o operador de subtração.
- **Multiplicação**: `\*` - Reconhece o operador de multiplicação.
- **Divisão**: `/` - Reconhece o operador de divisão.

## Exemplo de Uso

```bash
cd TPC6
python tpc6.py
```

### Se PLY não estiver instalado

```bash
pip install ply
```

### Formato do Arquivo de Entrada

O arquivo de entrada deve conter expressões matemáticas, uma por linha. Exemplos:

```
2 + 3
5 * 4 - 2
10 / 2 + 3
3.5 * 2
```

### Resultados Gerados

O programa gera um arquivo de saída com os resultados das expressões, formatados com uma casa decimal:

```
5.0
18.0
8.0
7.0
```

### Funcionalidades Suportadas

- Operações aritméticas básicas: adição, subtração, multiplicação e divisão.
- Precedência correta de operadores (multiplicação e divisão têm precedência sobre adição e subtração).
- Suporte para números decimais.
- Detecção de erros nas expressões (sintaxe inválida, divisão por zero).
- Processamento em lote de múltiplas expressões.

## Estrutura do Código

O código é organizado em várias seções:

1. **Análise Léxica**: Define os tokens e suas regras.
2. **Classes AST**: Implementa a classe `Exp` para representação e avaliação de expressões.
3. **Parser Recursivo Descendente**: Implementa a classe `Parser` para análise sintática.
4. **Lógica da Aplicação**: Funções para avaliar expressões e processar arquivos.
5. **Função Principal**: Ponto de entrada do programa.

## Testes

Foram realizados testes com diversas expressões para verificar o correto funcionamento do parser e do avaliador, incluindo:
- Operações básicas
- Operações com precedência
- Expressões com números decimais
- Sequências de operações

Todos os testes foram bem-sucedidos, demonstrando a robustez do implementação.

# Lista de Resultados
[Código Python](tpc6.py)
[Input](input.txt)
[Output](output.txt)