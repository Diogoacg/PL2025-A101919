import sys

def somador_on_off(text):
    soma = 0
    ativado = True
    num = ""
    output = []
    text = text.strip()

    i = 0
    while i < len(text):
        c = text[i]
        if c.lower() == "o":
            if i + 1 < len(text) and text[i+1].lower() == "n":
                ativado = True
                output.append("ON\n")
                i += 1
            elif i + 2 < len(text) and text[i+1].lower() == "f" and text[i+2].lower() == "f":
                ativado = False
                output.append("OFF\n")
                i += 2
            else:
                output.append(c)
        elif c.isdigit():
            if ativado:
                num += c
            output.append(c)
        elif c == "=":
            if num != "":
                soma += int(num)
                num = ""
            output.append(f"=\n>> {soma}\n")
        else:
            if num != "":
                soma += int(num)
                num = ""
            output.append(c)
        i += 1

    if num != "":
        soma += int(num)
    
    output.append(f"\n>> {soma}")
    print('\n'.join(''.join(output).strip().split('\n')))

if __name__ == "__main__":
    text = sys.stdin.read()
    somador_on_off(text)