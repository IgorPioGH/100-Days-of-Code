import tkinter as tk
from random import randint as rd
from tkinter import messagebox
from fornece_perguntas import lista_respostas, lista_perguntas, lista_perguntas_certas, lista_respostas_certas
import pandas as pd
BGCOLOR = "#B1DDC6"
i = 0

# ----- carregar perguntas e respostas ----- #
PERGUNTAS = lista_perguntas
RESPOSTAS = lista_respostas
PERGUNTAS_CERTAS = lista_perguntas_certas
RESPOSTAS_CERTAS = lista_respostas_certas
try:
    indice_pergunta = rd(0, len(PERGUNTAS)-1)
except ValueError:
    indice_pergunta = 0
    pergunta = ""
    resposta = ""
else:
    pergunta = PERGUNTAS[indice_pergunta]
    resposta = RESPOSTAS[indice_pergunta]

# ------ Setting GUI -------- #
window = tk.Tk()
window.title("FlashCard App")
window.geometry("+100+20")
window.config(padx=50, pady=50, background=BGCOLOR)

# -------- funcoes ---------- #
def nova_janela():
    janela_add_pergunta = tk.Toplevel(padx=50, pady=50, bg=BGCOLOR)
    janela_add_pergunta.title("Adicione Nova Pergunta")

    # Label entrada
    corpo_pergunta = tk.Label(janela_add_pergunta, text="Pergunta:", bg=BGCOLOR)
    corpo_pergunta.grid(column=0, row=0)
    entrada_pergunta = tk.Text(janela_add_pergunta, width=50, height=10)
    entrada_pergunta.grid(column=1, row=0,columnspan=2, pady=5)

    # Label entrada resposta
    corpo_resposta = tk.Label(janela_add_pergunta, text="Resposta:", bg=BGCOLOR)
    corpo_resposta.grid(column=0, row=1)
    entrada_resposta = tk.Text(janela_add_pergunta, pady=5, width=50, height=10)
    entrada_resposta.grid(column=1, row=1,columnspan=2, pady=5)

    # Botão fechar
    botao_fechar = tk.Button(janela_add_pergunta, text="Cancelar", command=janela_add_pergunta.destroy)
    botao_fechar.grid(column=0, row=2,columnspan=2, pady=5)
    # Botão adicionar
    botao_adicionar = tk.Button(janela_add_pergunta, text="Adicionar", command=lambda: nova_pergunta(entrada_pergunta, entrada_resposta, janela_add_pergunta))
    botao_adicionar.grid(column=2, row=2, pady=5)

def remove_pergunta():
    global RESPOSTAS, PERGUNTAS, RESPOSTAS_CERTAS, PERGUNTAS_CERTAS, indice_pergunta, pergunta
    if pergunta in PERGUNTAS_CERTAS:
        PERGUNTAS_CERTAS.pop(indice_pergunta)
        RESPOSTAS_CERTAS.pop(indice_pergunta)
    else:
        PERGUNTAS.pop(indice_pergunta)
        RESPOSTAS.pop(indice_pergunta)
    atualiza_pergunta()

def nova_pergunta(entrada_pergunta, entrada_resposta, janela):
    global RESPOSTAS, PERGUNTAS, resposta, pergunta, indice_pergunta, i
    nova_p = entrada_pergunta.get("1.0", "end-1c")
    nova_r = entrada_resposta.get("1.0", "end-1c")

    PERGUNTAS.append(nova_p)
    RESPOSTAS.append(nova_r)

    indice_pergunta = rd(0, len(PERGUNTAS)-1)
    pergunta = PERGUNTAS[indice_pergunta]
    resposta = RESPOSTAS[indice_pergunta]

    messagebox.showinfo(title="Message Add")

    i=0
    flip_card()
    janela.destroy()

def atualiza_pergunta():
    global pergunta, resposta, indice_pergunta, i

    # 80% de chance de tirar de PERGUNTAS, senão das CERTAS (se existirem)
    sorteio = rd(1, 10)

    if (len(PERGUNTAS) > 0) and (sorteio <= 8 or len(PERGUNTAS_CERTAS) == 0):
        indice_pergunta = rd(0, len(PERGUNTAS) - 1)
        pergunta = PERGUNTAS[indice_pergunta]
        resposta = RESPOSTAS[indice_pergunta]
    elif len(PERGUNTAS_CERTAS) > 0:
        indice_pergunta = rd(0, len(PERGUNTAS_CERTAS) - 1)
        pergunta = PERGUNTAS_CERTAS[indice_pergunta]
        resposta = RESPOSTAS_CERTAS[indice_pergunta]
    else:
        # Não há perguntas em lugar nenhum
        flash_card.config(text="Lista de perguntas vazia. Adicione mais.")
        return

    i = 0
    flip_card()


def acertou():
    global indice_pergunta
    try:
        RESPOSTAS_CERTAS.append(RESPOSTAS.pop(indice_pergunta))
        PERGUNTAS_CERTAS.append(PERGUNTAS.pop(indice_pergunta))
        # Se PERGUNTAS ou RESPOSTAS ficarem vazias
        if len(PERGUNTAS) == 0:
            indice_pergunta = 0
        else:
            indice_pergunta = rd(0, len(PERGUNTAS) - 1)
        atualiza_pergunta()
    except (ValueError, IndexError):
        atualiza_pergunta()

def errou():
    global pergunta, resposta, RESPOSTAS_CERTAS, PERGUNTAS_CERTAS, RESPOSTAS, PERGUNTAS, indice_pergunta
    if pergunta in PERGUNTAS_CERTAS:
        PERGUNTAS.append(PERGUNTAS_CERTAS.pop(indice_pergunta))
        RESPOSTAS.append(RESPOSTAS_CERTAS.pop(indice_pergunta))

    atualiza_pergunta()


def atualiza_card(novo_valor):
    flash_card.config(text=novo_valor)

def flip_card():
    global i
    if i % 2 !=0:
        atualiza_card(resposta)
        flash_card.config(image=back_image)

    else:
        atualiza_card(pergunta)
        flash_card.config(image=front_image)
    i+=1

def atualiza_dados():
    try:
        lista_df = [{pergunta: resposta} for pergunta, resposta in zip(PERGUNTAS, RESPOSTAS)]
        linhas = [(list(dicionario.keys())[0], list(dicionario.values())[0]) for dicionario in lista_df]
        df = pd.DataFrame(linhas, columns=["Perguntas", "Respostas"])
        df.to_csv("data/perguntas.csv")

        lista_df_certas = [{pergunta: resposta} for pergunta, resposta in zip(PERGUNTAS_CERTAS, RESPOSTAS_CERTAS)]
        linhas_certas = [(list(dicionario.keys())[0], list(dicionario.values())[0]) for dicionario in lista_df_certas]
        df_certas = pd.DataFrame(linhas_certas, columns=["Perguntas", "Respostas"])
        df_certas.to_csv("data/perguntas_certas.csv")
        window.destroy()
    except (IndexError, ValueError):
        print("Lista de perguntas vazia")
# -------- Images ----------- #
front_image = tk.PhotoImage(file="Images/card_front.png")
back_image = tk.PhotoImage(file="Images/card_back.png")
wrong_image = tk.PhotoImage(file="Images/wrong.png")
correct_image = tk.PhotoImage(file="Images/right.png")

#---------- Buttons --------#
flash_card = tk.Button(image=front_image,text="Clique para comecar", command=flip_card)
flash_card.config(font=("Ariel", 30, "bold"),compound="center", bg=BGCOLOR, borderwidth=0, wraplength=700, justify="center")
flash_card.grid(column=1,row=0, columnspan=2)

wrong_card = tk.Button(image=wrong_image, highlightthickness=0, command=errou)
wrong_card.grid(column=0, row=1)

correct_card = tk.Button(image=correct_image, highlightthickness=0, command=acertou)
correct_card.grid(column=3, row=1)

add_button = tk.Button(text="Adicionar", highlightthickness=0, width=15, height=5, font=("Ariel", 14, "bold"), bg=BGCOLOR,
                    command=nova_janela)
add_button.grid(column=2,row=1)

subtract_button = tk.Button(text="Remover", highlightthickness=0, width=15, height=5, font=("Ariel", 14, "bold"), bg=BGCOLOR,
                         command=remove_pergunta)
subtract_button.grid(column=1,row=1)


window.protocol("WM_DELETE_WINDOW", atualiza_dados)
window.mainloop()