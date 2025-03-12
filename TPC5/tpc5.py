import json
import datetime
import ply.lex as lex
import sys

# Configurar a codificação padrão para UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

class VendingMachineTokenizer:
    tokens = (
        'LISTAR',
        'MOEDA',
        'SELECIONAR',
        'ADICIONAR',
        'SAIR',
        'AJUDA',
        'COD',
        'NOME',
        'QUANTIDADE',
        'UNIDADE',
        'PRECO',
        'EURO',
        'CENT',
    )

    t_ignore = ' \t,'
    
    def t_LISTAR(self, t):
        r'LISTAR'
        return t
        
    def t_MOEDA(self, t):
        r'MOEDA'
        return t
        
    def t_SELECIONAR(self, t):
        r'SELECIONAR'
        return t
        
    def t_ADICIONAR(self, t):
        r'ADICIONAR'
        return t
        
    def t_SAIR(self, t):
        r'SAIR'
        return t
        
    def t_AJUDA(self, t):
        r'AJUDA'
        return t
    
    def t_COD(self, t):
        r'[A-Za-z]\d+'
        return t
        
    def t_NOME(self, t):
        r'"[^"]+"'
        t.value = t.value.strip('"')
        return t
    
    def t_EURO(self, t):
        r'[0-9]+[eE]'
        t.value = int(t.value[:-1]) * 100
        return t
        
    def t_CENT(self, t):
        r'[0-9]+[cC]'
        t.value = int(t.value[:-1])
        return t
    
    def t_QUANTIDADE(self, t):
        r'(?<!\.)\b\d+\b(?!\.)'
        t.value = int(t.value)
        return t

    def t_PRECO(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t
        
    def t_UNIDADE(self, t):
        r'[a-zA-Z]+'
        return t
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Carácter ilegal '{t.value[0]}'")
        t.lexer.skip(1)
        
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        
    def tokenize(self, data):
        self.lexer.input(data)
        return list(self.lexer)

def load_stock(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_stock(filename, stock):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(stock, file, indent=4, ensure_ascii=False)

def listar(stock):
    print("maq:")
    print(f"{'cod':<5} | {'nome':<20} | {'quantidade':<10} | {'preço':<5}")
    print("-" * 50)
    for item in stock:
        quant_str = str(item['quant'])
        if 'unidade' in item and item['unidade']:
            quant_str += item['unidade']
        print(f"{item['cod']:<5} | {item['nome']:<20} | {quant_str:<10} | {item['preco']:<5}")

def formatar_saldo(saldo_cents):
    euros = saldo_cents // 100
    cents = saldo_cents % 100
    if euros > 0:
        if cents > 0:
            return f"{euros}e{cents}c"
        return f"{euros}e"
    return f"{cents}c"

def selecionar(stock, saldo, cod):
    for item in stock:
        if item['cod'].upper() == cod.upper():
            if item['quant'] > 0:
                preco_cents = int(item['preco'] * 100)
                if saldo >= preco_cents:
                    item['quant'] -= 1
                    saldo -= preco_cents
                    print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {formatar_saldo(saldo)}; Pedido = {formatar_saldo(preco_cents)}")
            else:
                print(f"maq: Produto \"{item['nome']}\" esgotado")
            break
    else:
        print(f"maq: Produto com código \"{cod}\" não encontrado")
    return saldo

def devolver_troco(saldo):
    count_troco = {}
    valores = [('1e', 100), ('50c', 50), ('20c', 20), ('10c', 10), ('5c', 5), ('2c', 2), ('1c', 1)]
    
    for nome, valor in valores:
        quantidade = 0
        while saldo >= valor:
            quantidade += 1
            saldo -= valor
        if quantidade > 0:
            count_troco[nome] = quantidade
    
    if not count_troco:
        return "0c"
    
    troco_formatado = []
    for moeda, quantidade in count_troco.items():
        troco_formatado.append(f"{quantidade}x {moeda}")
    
    if len(troco_formatado) > 1:
        return ", ".join(troco_formatado[:-1]) + " e " + troco_formatado[-1]
    else:
        return troco_formatado[0]

def adicionar_produto(stock, cod, nome, quant, unidade, preco):
    for item in stock:
        if item['cod'].upper() == cod.upper():
            item['quant'] += quant
            item['unidade'] = unidade
            print(f"maq: Quantidade do produto \"{nome}\" atualizada. Nova quantidade: {item['quant']}{unidade}")
            return stock
    
    novo_produto = {
        "cod": cod,
        "nome": nome,
        "quant": quant,
        "unidade": unidade,
        "preco": preco
    }
    stock.append(novo_produto)
    print(f"maq: Novo produto \"{nome}\" adicionado ao stock.")
    return stock

def main():
    tokenizer = VendingMachineTokenizer()
    tokenizer.build()
    
    stock = load_stock('stock.json')
    saldo = 0
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip()
        tokens = tokenizer.tokenize(comando)
        
        if not tokens:
            continue
            
        if tokens[0].type == 'LISTAR':
            listar(stock)
            
        elif tokens[0].type == 'MOEDA':
            moedas_adicionadas = False
            for token in tokens[1:]:
                if token.type == 'EURO':
                    saldo += token.value
                    moedas_adicionadas = True
                elif token.type == 'CENT':
                    saldo += token.value
                    moedas_adicionadas = True
            
            if not moedas_adicionadas:
                print("maq: Nenhuma moeda válida inserida")
            
            print(f"maq: Saldo = {formatar_saldo(saldo)}")
            
        elif tokens[0].type == 'SELECIONAR':
            if len(tokens) > 1 and tokens[1].type == 'COD':
                saldo = selecionar(stock, saldo, tokens[1].value)
                print(f"maq: Saldo = {formatar_saldo(saldo)}")
            else:
                print("maq: Código de produto não especificado")
                
        elif tokens[0].type == 'ADICIONAR':
            if len(tokens) >= 5:
                cod = nome = None
                quant = 0
                unidade = ""
                preco = 0.0

                for token in tokens[1:]:
                    if token.type == 'COD' and cod is None:
                        cod = token.value.upper()
                    elif token.type == 'NOME' and nome is None:
                        nome = token.value
                    elif token.type == 'QUANTIDADE' and quant == 0:
                        quant = token.value
                    elif token.type == 'UNIDADE' and unidade == "":
                        unidade = token.value
                    elif token.type == 'PRECO' and preco == 0.0:
                        preco = token.value
                
                if cod and nome and quant > 0 and preco > 0:
                    stock = adicionar_produto(stock, cod, nome, quant, unidade, preco)
                else:
                    print("maq: Parâmetros insuficientes ou inválidos")
            else:
                print("maq: Formato inválido. Use: ADICIONAR codigo \"nome\" quantidade preco")
                
        elif tokens[0].type == 'SAIR':
            if saldo > 0:
                troco = devolver_troco(saldo)
                print(f"maq: Pode retirar o troco: {troco}.")
            print("maq: Até à próxima")
            save_stock('stock.json', stock)
            break
            
        elif tokens[0].type == 'AJUDA':
            print("maq: Comandos disponíveis:")
            print("  LISTAR - Mostra os produtos disponíveis")
            print("  MOEDA <valores> - Insere moedas (ex: 1e, 50c, 20c)")
            print("  SELECIONAR <código> - Seleciona um produto pelo código")
            print("  ADICIONAR <código> \"<nome>\" <quantidade> [<unidade>] <preço> - Adiciona um produto ao stock")
            print("  SAIR - Sai do sistema e devolve o troco")
            print("  AJUDA - Mostra esta mensagem de ajuda")
            
        else:
            print("maq: Comando desconhecido. Digite AJUDA para ver os comandos disponíveis.")

if __name__ == "__main__":
    main()