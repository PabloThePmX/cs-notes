import pandas as pd
from os import system

system("cls")

df = pd.read_csv("First Nanodegree\Pensamento Computacional\Python\Pandas\sociodem_fake_2.csv", sep=";")

salario = {
    "Até 1 salário-mínimo (até R$ 1.320)": 1,
    "De 1 a 2 salários-mínimos (de R$1.320,00 até R$ 2.640,00)": 2,
    "De 2 a 3 salários-mínimos (de R$ 2.640,00 até R$ 3.960,00)": 3,
    "De 3 a 4 salários-mínimos (de R$3.960,00 até R$ 5.280,00)": 4,
    "De 4 a 5 salários-mínimos (de R$5.280,00 até R$ 6.600,00)": 5, 
    "De 5 a 6 salários-mínimos (de R$6.600,00 até R$7.920,00)": 6,
    "De 6 a 7 salários-mínimos (de R$7.920,00 até R$9.240,00)": 7,
    "De 7 a 8 salários-mínimos (de R$9.240,00 até R$10.560,00)": 8,
    "De 8 a 9 salários-mínimos (de R$10.560,00 até R$11.880,00)": 9,
    "Mais de 9 salários-mínimos (mais de R$ 11.880,00).": 10,
    "Não sei": 11
}

df["precisa_bolsa_estudos"] = df["renda_familiar"].apply(lambda value: "Sim" if salario[value] <= 2 else "Não")
df_filtrado = df[(df["precisa_bolsa_estudos"] == "Sim")]
print(df_filtrado[["cor_pele","precisa_bolsa_estudos"]])