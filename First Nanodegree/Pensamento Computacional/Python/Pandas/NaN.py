import pandas as mario

# Quando tem None, ele vai transformar os valores em float, par ver se o valor realmente não existe, ou é menor que 0
dados = {
    "valores_1": [1,2,3,4],
    "valores_2": [1,2,None,4] # NaN = Not a number
}

# df é o nome padrão, porém se temos mais que um df, devemos colocar outros nomes
df =  mario.DataFrame(dados)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
print(df["valores_1"].isna())

# axis = 0, linha; axis = 1, colunas