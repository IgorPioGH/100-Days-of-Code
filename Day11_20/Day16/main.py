from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cardapio = Menu()
maquina_cafe = CoffeeMaker()
maquina_dinheiro = MoneyMachine()

is_on = True
while is_on:
    pedido = input(f"Qual cafe voce gostaria de pedir? ({cardapio.get_items()}): ")
    if pedido == 'report':
        maquina_cafe.report()
        maquina_dinheiro.report()
    elif pedido == "off":
        is_on = False
    else:
        pedido_menu = cardapio.find_drink(pedido)
        if maquina_cafe.is_resource_sufficient(pedido_menu):
            if maquina_dinheiro.make_payment(pedido_menu.cost):
                maquina_cafe.make_coffee(pedido_menu)