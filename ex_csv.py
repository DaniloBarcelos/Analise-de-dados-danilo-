# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)
print("hello")
import pandas as pd
df = pd.read_csv(r"C:\Users\danil\OneDrive\Área de Trabalho\Analise de dados\notas(1).csv")
# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================


# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
df.shape
# 2. Quais são os tipos de dados? 
df.dtypes
# 3. Existe coluna com valores ausentes?
df.isnull().sun()
# 4. Qual é o período de anos disponível? 
df.colunas
df.loc[:,"year"].unique()
# 5. Quantos países diferentes
# existem?
df.loc[:,"country"].unique()

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
df.coluna
df.loc[:,"score"].mean()
# 2. Maior score 
df.loc[:,"score"].max()
# 3.Menor score 
df.loc[:,"score"].min()
# 4. Média do score por ano 
df.groupby("year")["score"].mean()
# 5. Desvio padrão do score

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
df.columns
df.loc[:,["institution","world_ranck"]].sort,values("world_ranck")
# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
filtro = df["country"]=="Brazil"
df_brazil = df.loc[filtro,["institution","world_rank","country"]].sort_values("world_rank")
# 3. Mostre universidades com score maior que 90 
df_score_90 = df.loc[df["score"] > 90,["institution", "world_rank", "score", "country"]]
df_score_90
# 4. Mostre universidades dos EUA com score maior que 80
filtro = df["country"]=="USA"
filtro_score = df["score"] > 80
df_usa_80 = df.loc[filtro & filtro_score]
df_usa_80

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution,
# country e score 
# 2. Mostre universidades entre rank 50 e 100 
# 3. Mostre universidades cujo país é “United Kingdom”

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
# 2. Qual percentual do dataset é nulo? 
# 3. Remova linhas com broad_impact nulo 
# 4. Preencha valores nulos com a média 
# 5. Compare a média antes e depois do preenchimento

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
# 2. País com maior média de score 
# 3. Quantidade de universidades por país 
# 4. Top 10 países com mais universidades

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
# 2. Qual ano teve maior média? 
# 3. Faça um gráfico da evolução do score médio ao longo do tempo
