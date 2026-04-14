import pandas as pd

# Questão 1:
# Ler o arquivo salaries.csv em um DataFrame chamado df
df = pd.read_csv("salaries.csv")

# Questão 2:
# Qual o maior salário ("salary_in_usd") no dataset?
maior_salario = df["salary_in_usd"].max()
print("Maior salário:", maior_salario)

# Questão 3:
# Quantos funcionários são "Data Scientist" ("job_title")?
data_scientists = df[df["job_title"] == "Data Scientist"].shape[0]
print("Quantidade de Data Scientists:", data_scientists)

# Questão 4:
# Quantos cargos ("job_title") possuem a palavra "Engineer"?
cargos_engineer = df["job_title"].str.contains("Engineer").sum()
print("Cargos com 'Engineer':", cargos_engineer)

# Questão 5:
# Mostrar funcionários ("experience_level") Senior ("SE") 
# que ganham ("salary_in_usd") mais que 100 mil
seniors = df[(df["experience_level"] == "SE") & (df["salary_in_usd"] > 100000)]
print(seniors)