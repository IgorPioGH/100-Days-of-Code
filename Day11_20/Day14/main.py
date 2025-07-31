from game_data import data
from art import logo, vs
import random

# funcoes
def escolher_random_data(data):
    return random.choice(data)

# Exibe os valores a comparar
def exibir_comparacoes(item1, item2):
    print(f'A: {item1["name"]}, a {item1["description"]} from {item1["country"]}')
    print(vs)
    print(f'B: {item2["name"]}, a {item2["description"]} from {item2["country"]}')

def checa_palpite(item1, item2, palpite):
    if palpite == 'a' and item1['follower_count'] > item2['follower_count']:
        print("You right!")
        return 1
    elif palpite == 'b' and item1['follower_count'] < item2['follower_count']:
        print("You right")
        return 2
    else:
        return 0

def recebe_palpite():
    palpite = input("'A' or 'B' has more followers: ").lower()
    return palpite

def novo_round(item1, item2):
    item1 = item2
    item2 = escolher_random_data(data)
    return item1, item2


def play_game():
    # variaveis
    a_item = escolher_random_data(data)
    b_item = escolher_random_data(data)
    pontuacao_usuario = 0
    eh_game_over = False
    while not eh_game_over:
        print(logo)
        exibir_comparacoes(a_item, b_item)
        palpite_usuario = recebe_palpite()
        resultado_palpite = checa_palpite(a_item, b_item,palpite_usuario)
        if resultado_palpite == 1:
            pontuacao_usuario += 1
            print(f"Você tem {pontuacao_usuario} pontos.")
            a_item, b_item = novo_round(b_item, a_item)
            eh_game_over = False
        elif resultado_palpite == 2:
            pontuacao_usuario += 1
            print(f"Você tem {pontuacao_usuario} pontos.")
            a_item, b_item = novo_round(a_item, b_item)
            eh_game_over = False
        else:
            eh_game_over = True
    print(f"Você perdeu! Sua pontuação foi de {pontuacao_usuario} pontos")
    return

play_game()