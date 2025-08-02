from data import MENU, profit, resources


# verificar se os ingredientes são suficiente
def ingredientes_suficiente(lista_ingredientes):
    for item in lista_ingredientes:
        if lista_ingredientes[item] > resources[item]:
            print(f"Desculpe, não temos {item} o suficiente")
            return False
    return True


# recebe o pagamento
def processa_moedas():
    """Retorna o valor total das moedas inseridas"""
    print("Por favor insira as moedas")
    total = int(input("Quantas moedas de R$0.25? ")) * 0.25
    total += int(input("Quantas moedas de R$0.1? ")) * 0.1
    total += int(input("Quantas moedas de R$0.05? ")) * 0.05
    total += int(input("Quantas moedas de R$0.01? ")) * 0.01
    return total

# verificar se o pagamento é suficiente
def pagamento_eh_suficiente(pagamento, valor_cafe):
    """Retorna True se o pagamento for o suficiente e False se nao for"""
    if pagamento >= valor_cafe:
        troco = round(pagamento - valor_cafe, 2)
        print(f"Aqui esta seus R${troco} de troco")
        global profit
        profit += valor_cafe
        return True
    else:
        print("Desculpe dinheiro insuficiente. Dinheiro estornado")
        return False

# funcao para fazer o cafe (retirar os ingredientes)
def fazer_cafe(nome_cafe, lista_ingredientes):
    """Desconta os itens da lista de ingredientes disponíveis,
    recebe o nome do cafe e a lista de ingrdientes que ele utiliza"""
    for item in lista_ingredientes:
        resources[item] -= lista_ingredientes[item]
    print("Aqui esta seu café. Aproveite!")

# logica do funcionamento da maquina
esta_ligada = True
while esta_ligada:
    pedido = input("Qual café você deseja? (espresso/latte/cappuccino) ")
    if pedido == 'off':
        esta_ligada = False
    elif pedido == 'report':
        print(f"Água: {resources['water']}ml")
        print(f"Leite: {resources['milk']}ml")
        print(f"Café: {resources['coffee']}g")
        print(f"Dinheiro: R${profit}")
    else:
        bebida = MENU[pedido]
        print(f"O {pedido} custa: {bebida['cost']}")
        if ingredientes_suficiente(bebida["ingredients"]):
            dinheiro = processa_moedas()
            if pagamento_eh_suficiente(dinheiro, bebida['cost']):
                fazer_cafe(pedido, bebida["ingredients"])
