# Calculadora de Expressões Matemáticas

**Data:** 20 de março de 2025

# Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

# Resumo

Este programa implementa uma calculadora de expressões matemáticas que processa um arquivo de entrada contendo expressões matemáticas e gera um arquivo de saída com os resultados dos cálculos. O programa utiliza a biblioteca PLY (Python Lex-Yacc) para análise léxica e sintática das expressões.

## Algoritmo

O algoritmo utiliza a biblioteca PLY para definir e reconhecer tokens nas expressões matemáticas. As principais etapas do algoritmo são:

1. **Análise Léxica** ([em exp_lex.py](exp_lex.py)):
   - Definição dos tokens: `NUMBER`, `PLUS`, `MINUS`, `MULTIPLY`, `DIVIDE`.
   - Definição de expressões regulares para cada tipo de token.
   - Processamento de números com suporte para decimais.
   - Tratamento de espaços em branco e erros léxicos.

2. **Análise Sintática** ([em exp_sin.py](exp_sin.py)):
   - Definição de regras gramaticais usando PLY Yacc.
   - Implementação de operações aritméticas (+, -, *, /).
   - Definição de regras de precedência (multiplicação/divisão antes de adição/subtração).
   - Tratamento de erros sintáticos.

3. **Processamento de Arquivos** ([em tpc6.py](tpc6.py)):
   - Leitura de expressões de um arquivo de entrada.
   - Avaliação de cada expressão utilizando o parser.
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
2 - 3
5 * 4 - 2
10 / 2 + 3
3.5 * 2
```

### Resultados Gerados

O programa gera um arquivo de saída com os resultados das expressões, formatados com uma casa decimal:

```
-1.0
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

O código é organizado em três arquivos principais:

1. **exp_lex.py**: Contém a análise léxica usando PLY Lex.
   - Define os tokens e suas regras de reconhecimento.
   - Implementa o tratamento de números e operadores.

2. **exp_sin.py**: Contém a análise sintática usando PLY Yacc.
   - Define as regras gramaticais para expressões matemáticas.
   - Implementa as operações aritméticas.
   - Define a precedência dos operadores.
   - Exporta a função `evaluate_expression()` para avaliar expressões.

3. **tpc6.py**: Contém a lógica principal do programa.
   - Processamento de arquivos de entrada e saída.
   - Tratamento de erros e formatação de resultados.
   - Implementa a interface principal do programa.

## Vantagens da Abordagem PLY

1. **Clareza e Manutenção**: Separando o código em componentes de análise léxica e sintática, o programa é mais fácil de entender e manter.
2. **Extensibilidade**: Novas operações ou funcionalidades podem ser adicionadas facilmente.
3. **Tratamento de Erros**: PLY fornece mecanismos robustos para detecção e tratamento de erros.
4. **Precedência de Operadores**: Facilmente definida através da tupla `precedence`.

## Testes

Foram realizados testes com diversas expressões para verificar o correto funcionamento do parser e do avaliador, incluindo:
- Operações básicas
- Operações com precedência
- Expressões com números decimais
- Sequências de operações

Todos os testes foram bem-sucedidos, demonstrando a robustez da implementação. Os resultados dos testes são consistentes com a matemática padrão, respeitando a precedência de operadores e as regras de associatividade da esquerda para a direita.

## Limitações e Possíveis Melhorias

- Adicionar suporte para parênteses para permitir controle explícito da precedência.
- Implementar funções matemáticas (sin, cos, log, etc.).
- Adicionar suporte para variáveis e atribuição.
- Implementar interface gráfica para uso mais amigável.

# Lista de Resultados
- [exp_lex.py](Analisador_Lexico)
- [exp_sin.py](Analisador_Sintatico)
- [tpc6.py](Programa_Principal)
- [input.txt](Input)
- [output.txt](Output)