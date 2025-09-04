##################### Extra Hard Starting Project ######################
import smtplib
import os
from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import random as rd
load_dotenv()
moldes = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = os.getenv("MY_EMAIL_KEY")
CODE = os.getenv("CODE_KEY")
hoje = dt.datetime.today()
mes_hoje = hoje.month
dia_hoje = hoje.day
ano_hoje = hoje.year

def enviar_email(arq_texto, nome_destino, email_destino):
    with open(f"letter_templates/{arq_texto}") as molde_file:
        conteudo = molde_file.read()
        nova_msg = conteudo.replace('[NAME]', nome_destino)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=CODE)
        connection.sendmail(
            to_addrs=email_destino,
            from_addr=MY_EMAIL,
            msg=f"Subject:Happy Birthday!\n\n{nova_msg}"
        )
        print(f"Email enviado para {email_destino}")

df = pd.read_csv("birthdays.csv")
df_dicionarios = df.to_dict(orient="records")
for i in range(len(df_dicionarios)):
    mes_csv = int(df_dicionarios[i]["month"])
    dia_csv = int(df_dicionarios[i]["day"])
    if mes_csv == mes_hoje and dia_csv == dia_hoje:
        nome = df_dicionarios[i]["name"]
        email = df_dicionarios[i]["email"]
        arquivo_leitura = rd.choice(moldes)
        enviar_email(arquivo_leitura, nome, email)



