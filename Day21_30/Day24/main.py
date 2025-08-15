#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# lista de nomes
lista_nomes = []
with open("Input/Names/invited_names.txt", "r", encoding='utf-8') as file:
    content = file.readlines()
    for nome in content:
        lista_nomes.append(nome)


#fazendo o texto
for nome in lista_nomes:
    nome = nome.replace("\n","")
    corpo_letter = []
    # acessando corpo da carta
    with open("Input/Letters/starting_letter.txt", "r", encoding='utf-8') as file:
        content = file.readlines()
        for linha in content:
            corpo_letter.append(linha)
            corpo_letter[0] = f"Dear {nome},\n"
    with open(f"Output/ReadyToSend/{nome}.txt", "w", encoding='utf-8') as file:
        for linhas in corpo_letter:
            file.write(linhas)