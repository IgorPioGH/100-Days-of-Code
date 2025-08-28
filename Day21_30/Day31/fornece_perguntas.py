import pandas as pd
import random as rd

df = pd.read_csv("data/perguntas.csv")
df_certas = pd.read_csv("data/perguntas_certas.csv")
dicionarios = df.to_dict(orient="records")
dicionarios_certos = df_certas.to_dict(orient="records")

try:
    aleatorio = rd.randint(0, len(dicionarios) - 1)
except (IndexError, ValueError):
    lista_perguntas = [dicionario["Perguntas"] for dicionario in dicionarios_certos]
    lista_respostas = [dicionario["Respostas"] for dicionario in dicionarios_certos]
    lista_perguntas_certas = []
    lista_respostas_certas = []
else:
    lista_perguntas = [dicionario["Perguntas"] for dicionario in dicionarios]
    lista_respostas = [dicionario["Respostas"] for dicionario in dicionarios]
    lista_perguntas_certas = [dicionario["Perguntas"] for dicionario in dicionarios_certos]
    lista_respostas_certas = [dicionario["Respostas"] for dicionario in dicionarios_certos]