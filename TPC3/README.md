# Conversor de Markdown para HTML

**Data:** 26 de fevereiro de 2025

# Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

# Resumo

Este programa tem como objetivo converter um arquivo Markdown (`.md`) em um arquivo HTML (`.html`). Ele suporta várias funcionalidades do Markdown, incluindo cabeçalhos, listas ordenadas e não ordenadas, blocos de código, citações, texto riscado, texto sublinhado, tabelas, caracteres especiais e linhas horizontais.

## Funcionalidades Suportadas

- **Cabeçalhos:** Níveis de 1 a 6 (`#`, `##`, `###`, `####`, `#####`, `######`).
- **Listas Ordenadas:** Listas numeradas (`1.`, `2.`, `3.`, etc.).
- **Listas Não Ordenadas:** Listas com marcadores (`-`, `*`, `+`).
- **Blocos de Código:** Blocos de código delimitados por três crases (```` ``` ````).
- **Citações:** Citações iniciadas com `>`.
- **Texto Riscado:** Texto riscado delimitado por `~~`.
- **Texto Sublinhado:** Texto sublinhado delimitado por `<u>...</u>`.
- **Tabelas:** Tabelas delimitadas por `|`.
- **Caracteres Especiais:** Caracteres especiais escapados (`\*`, `\_`, `\``, `\[`, `\]`).
- **Linhas Horizontais:** Linhas horizontais (`---`, `***`, `___`).
- **Links e Imagens:** Links (`[texto](url)`) e imagens (`![alt](url)`).
- **Código em Linha:** Código em linha delimitado por crases (`\``).

## Algoritmo

O algoritmo utiliza expressões regulares (regex) para processar o arquivo Markdown de forma eficiente e precisa. As principais etapas do algoritmo são:

1. **Leitura do Arquivo Markdown:** O conteúdo do arquivo é lido linha por linha.
2. **Identificação de Elementos Markdown:** Utiliza-se regex para identificar e converter elementos Markdown em HTML.
3. **Processamento dos Dados:** Os elementos são processados e convertidos para HTML, incluindo cabeçalhos, listas, blocos de código, citações, texto riscado, texto sublinhado, tabelas, caracteres especiais e linhas horizontais.

### Expressões Regulares Utilizadas

#### Cabeçalhos
```regex
^(#{1,6})\s+(.*)
```
- `^` - Início da linha.
- `(#{1,6})` - Captura de 1 a 6 caracteres `#`, indicando o nível do cabeçalho.
- `\s+` - Um ou mais espaços em branco.
- `(.*)` - Captura o restante da linha, que é o conteúdo do cabeçalho.

#### Listas Ordenadas
```regex
^(\d+)\.\s+(.*)
```
- `^` - Início da linha.
- `(\d+)` - Captura um ou mais dígitos, indicando o número do item da lista.
- `\.` - Um ponto literal.
- `\s+` - Um ou mais espaços em branco.
- `(.*)` - Captura o restante da linha, que é o conteúdo do item da lista.

#### Listas Não Ordenadas
```regex
^-\s+(.*)
```
- `^` - Início da linha.
- `-` - Um caractere `-` literal, indicando um item de lista não ordenada.
- `\s+` - Um ou mais espaços em branco.
- `(.*)` - Captura o restante da linha, que é o conteúdo do item da lista.

#### Citações
```regex
^>\s+(.*)
```
- `^` - Início da linha.
- `>` - Um caractere `>` literal, indicando uma citação.
- `\s+` - Um ou mais espaços em branco.
- `(.*)` - Captura o restante da linha, que é o conteúdo da citação.

#### Linhas Horizontais
```regex
^-{3,}$|^\*{3,}$|^_{3,}$
```
- `^-{3,}$` - Captura uma linha que contém três ou mais hifens (`-`).
- `|` - Ou.
- `^\*{3,}$` - Captura uma linha que contém três ou mais asteriscos (`*`).
- `|` - Ou.
- `^_{3,}$` - Captura uma linha que contém três ou mais sublinhados (`_`).

#### Tabelas
```regex
^\|.*\|$
```
- `^` - Início da linha.
- `\|` - Um caractere `|` literal.
- `.*` - Captura zero ou mais caracteres.
- `\|` - Um caractere `|` literal.
- `$` - Fim da linha.

#### Processamento Inline
```regex
!\[([^\]]*?)\]\((.*?)\)
\[([^\]]*?)\]\((.*?)\)
\*\*(.*?)\*\*
\*(.*?)\*
~~(.*?)~~
<u>(.*?)</u>
`([^`]+)`
```
- `!\[([^\]]*?)\]\((.*?)\)` - Captura imagens:
  - `!\[` - Um literal `![`.
  - `([^\]]*?)` - Captura o texto alternativo da imagem.
  - `\]` - Um literal `]`.
  - `\(` - Um literal `(`.
  - `(.*?)` - Captura a URL da imagem.
  - `\)` - Um literal `)`.

- `\[([^\]]*?)\]\((.*?)\)` - Captura links:
  - `\[([^\]]*?)\]` - Captura o texto do link.
  - `\((.*?)\)` - Captura a URL do link.

- `\*\*(.*?)\*\*` - Captura texto em negrito:
  - `\*\*` - Dois asteriscos literais.
  - `(.*?)` - Captura o texto em negrito.
  - `\*\*` - Dois asteriscos literais.

- `\*(.*?)\*` - Captura texto em itálico:
  - `\*` - Um asterisco literal.
  - `(.*?)` - Captura o texto em itálico.
  - `\*` - Um asterisco literal.

- `~~(.*?)~~` - Captura texto riscado:
  - `~~` - Dois til literais.
  - `(.*?)` - Captura o texto riscado.
  - `~~` - Dois til literais.

- `<u>(.*?)</u>` - Captura texto sublinhado:
  - `<u>` - Literal `<u>`.
  - `(.*?)` - Captura o texto sublinhado.
  - `</u>` - Literal `</u>`.

- `` `([^`]+)` `` - Captura código em linha:
  - `` ` `` - Um literal `` ` ``.
  - `([^`]+)` - Captura o texto do código em linha.
  - `` ` `` - Um literal `` ` ``.

## Exemplo de Utilização

```bash
python tpc3.py exemplo.md
```

## Exemplo de Entrada e Saída

### Entrada:
Arquivo Markdown (`exemplo.md`) contendo informações formatadas em Markdown.
Amostra do arquivo:

````markdown
# Exemplo de um Titulo

Este é um **exemplo** de texto em markdown bold.

Este é um *exemplo* de texto em markdown itálico.

# Exemplo de um **Título** com *énfase*

## Exemplo de um Subtítulo

Aqui está uma lista numerada:

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](https://www.uminho.pt/PT)

Como se vê na imagem seguinte por link: ![imagem dum coelho](http://www.coelho.com).

Ou na imagem seguinte por ficheiro: ![imagem dum coelho](coelho.jpg)

# Cabeçalho de nível 1
## Cabeçalho de nível 2
### Cabeçalho de nível 3
#### Cabeçalho de nível 4
##### Cabeçalho de nível 5
###### Cabeçalho de nível 6

Aqui está um exemplo de `código em linha`.

```
// Isto é um bloco de código
int main() {
    printf("Hello, World!");
    return 0;
}
```

> Esta é uma citação.
> Pode ter múltiplas linhas.

Este é um ~~texto riscado~~.

Este é um <u>texto sublinhado</u>.

Caracteres especiais: \* \_ \` \[ \]

---
***
___

**Texto em negrito e *itálico*** com [link](http://www.exemplo.com) e ![imagem](http://www.exemplo.com/imagem.jpg).
````

### Saída:
Arquivo HTML (`output.html`) gerado a partir do arquivo Markdown. Amostra do arquivo:

```html
<h1>Exemplo de um Titulo</h1>
Este é um <b>exemplo</b> de texto em markdown bold.<br>
Este é um <i>exemplo</i> de texto em markdown itálico.<br>
<h1>Exemplo de um <b>Título</b> com <i>énfase</i></h1>
<h2>Exemplo de um Subtítulo</h2>
Aqui está uma lista numerada:<br>
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
Como pode ser consultado em <a href="https://www.uminho.pt/PT">página da UC</a><br>
Como se vê na imagem seguinte por link: <img src="http://www.coelho.com" alt="imagem dum coelho"/><br>
Ou na imagem seguinte por ficheiro: <img src="coelho.jpg" alt="imagem dum coelho"/><br>
<h1>Cabeçalho de nível 1</h1>
<h2>Cabeçalho de nível 2</h2>
<h3>Cabeçalho de nível 3</h3>
<h4>Cabeçalho de nível 4</h4>
<h5>Cabeçalho de nível 5</h5>
<h6>Cabeçalho de nível 6</h6>
Aqui está um exemplo de <code>código em linha</code>.<br>
<pre>
// Isto é um bloco de código
int main() {
    printf("Hello, World!");
    return 0;
}
</pre>
<blockquote>Esta é uma citação.</blockquote>
<blockquote>Pode ter múltiplas linhas.</blockquote>
Este é um <del>texto riscado</del>.<br>
Este é um <u>texto sublinhado</u>.<br>
<table>
<tr><td>Cabeçalho 1</td><td>Cabeçalho 2</td></tr>
<tr><td>Linha 1</td><td>Conteúdo 1</td></tr>
<tr><td>Linha 2</td><td>Conteúdo 2</td></tr>
</table>
Caracteres especiais: \* \_ \` \[ \]<br>
<hr>
<hr>
<hr>
<b>Texto em negrito e <i>itálico</b></i> com <a href="http://www.exemplo.com">link</a> e <img src="http://www.exemplo.com/imagem.jpg" alt="imagem"/><br>
```

## Lista de Resultados
- [Código Python](tpc3.py)
- [Exemplo Markdown](exemplo.md)
- [Exemplo HTML](output.html)
- [Imagem de Coelho](coelho.jpg)