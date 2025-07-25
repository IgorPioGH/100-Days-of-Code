import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista_jogadas = [rock, paper, scissors]
print("Bem vindo ao jogo de pedra, papel ou tesoura!")
print("Digite 0 para escolher pedra")
print("Digite 1 para escolher papel")
print("Digite 2 para escolher tesoura")

escolha_usuario = int(input())
escolha_computador = random.randint(0,2)

print(f'Sua escolha: \n{lista_jogadas[escolha_usuario]}')

print(f'Jogada do computador: \n{lista_jogadas[escolha_computador]}')

if escolha_computador == escolha_usuario:
    print('O jogo empatou!')
else:
    if escolha_computador == 0 and escolha_usuario == 1:
        print('Parabéns! Você ganhou!')
    elif escolha_computador == 1 and escolha_usuario == 2:
        print('Parabéns! Você ganhou!')
    elif escolha_computador == 2 and escolha_usuario == 0:
        print('Parabéns! Você ganhou!')
    else:
        print('Que pena! O computador ganhou!')
        print('Excluindo C:/system32/.')
        input()