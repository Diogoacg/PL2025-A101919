import re

def somador_on_off(texto):
    soma_total = 0
    somador_ligado = True 

    for match in re.finditer(r'\d+|[Oo][Nn]|[Oo][Ff][Ff]|=', texto):
        token = match.group()
        
        if re.fullmatch(r'[Oo][Nn]', token):
            somador_ligado = True
        elif re.fullmatch(r'[Oo][Ff][Ff]', token):
            somador_ligado = False
        elif re.fullmatch(r'\d+', token) and somador_ligado:
            soma_total += int(token)
        elif re.fullmatch(r'=', token):
            print(soma_total)

# Exemplo de uso
texto = input("Indique o texto para realizar a soma: ")
somador_on_off(texto)