import pandas as pd
# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?

df = pd.read_csv("titanic.csv")
print("Primeiras linhas do DataFrame:")
print(df.head())


# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")

mulheres = df[df["Sex"] == "female"]
print("\nPassageiras mulheres:")
print(mulheres)

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")

sobreviventes = df[df["Survived"] == 1].shape[0]
print("\nNúmero de sobreviventes:")
print(sobreviventes)

# Questão 4:
# Quantos Homens Sobreviveram?

homens_sobreviveram = df[(df["Sex"] == "male") & (df["Survived"] == 1)].shape[0]
print("\nHomens que sobreviveram:")
print(homens_sobreviveram)

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name"

john = df[df["Name"].str.contains("John", case=False, na=False)].shape[0]
print("\nQuantidade de passageiros com nome John:")
print(john)
