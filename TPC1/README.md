# Somador On/Off

**Data:** 11 de fevereiro de 2025

## Autor

**Nome:** Diogo Afonso Costa Gonçalves  
**Número:** a101919  

## Resumo

Este programa tem como objetivo somar sequências de dígitos num dado texto passado como argumento, seguindo as seguintes regras:

- O programa começa com a soma ativada, mas pode ser controlada através dos comandos `"On"` e `"Off"` em qualquer combinação de letras maiúsculas ou minúsculas.
- Quando o programa encontra `"On"`, a soma é ativada.
- Quando encontra `"Off"`, a soma é desativada.
- Sempre que encontra um número enquanto a soma está ativada, este é adicionado ao total.
- O sinal `"="` faz com que o resultado acumulado seja impresso no stdout.

## Exemplo de Utilização

```bash
echo "Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7= dias para o fazer... ON Cada trabalho destes vale 0.25 valores da nota final!" | python tpc1.py
```

## Exemplo de Entrada e Saída

### Entrada:
```bash
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7= dias para o fazer... ON Cada trabalho destes vale 0.25 valores da nota final!
```

### Saída:
```bash
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=
>> 2032
OFF
 E deu-nos 7=
>> 2032
 dias para o fazer... ON
 Cada trabalho destes vale 0.25 valores da nota final!
>> 2057
```

## Ficheiro
- [Código Python](tpc1.py)