import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
dict_alphabet = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Digite seu nome: ").upper()

lista_final = [dict_alphabet[letra] for letra in user_input]
print(lista_final)
