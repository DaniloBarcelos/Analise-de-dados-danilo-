# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)
print("hello")
import pandas as pd
df = pd.read_csv(r"C:\Users\danil\OneDrive\Área de Trabalho\Analise de dados\notas(1).csv")
# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================


print("hello")
import pandas as pd

df = pd.read_csv(r"C:\Users\danil\OneDrive\Área de Trabalho\Analise de dados\notas(1).csv")

# 1. Quantas linhas e colunas existem?
df.shape

# 2. Quais são os tipos de dados?
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isnull().sum()

# 4. Qual é o período de anos disponível?
df.columns
df.loc[:, "year"].unique()

# 5. Quantos países diferentes existem?
df.loc[:, "country"].unique()


# Exercício 2 – Estatísticas Gerais 

# 1. Média do score 
df["score"].mean()

# 2. Maior score 
df["score"].max()

# 3. Menor score 
df["score"].min()

# 4. Média do score por ano 
df.groupby("year")["score"].mean()

# 5. Desvio padrão do score
df["score"].std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 

# 1. Mostre as 10 melhores universidades do mundo (menor world_rank)
top10 = (
    df.loc[:, ["institution", "world_rank"]]
      .sort_values("world_rank")
      .head(10)
)
top10


# 2. Mostre as 5 melhores universidades do Brasil (se existirem)
df_brazil = (
    df.loc[df["country"] == "Brazil", 
           ["institution", "world_rank", "country"]]
      .sort_values("world_rank")
      .head(5)
)
df_brazil


# 3. Mostre universidades com score maior que 90 
df_score_90 = df.loc[
    df["score"] > 90,
    ["institution", "world_rank", "score", "country"]
]
df_score_90


# 4. Mostre universidades dos EUA com score maior que 80
df_usa_80 = df.loc[
    (df["country"] == "USA") & (df["score"] > 80),
    ["institution", "world_rank", "score", "country"]
]
df_usa_80


# %%
# Exercício 4 – Seleção Avançada 

# 1. Mostre apenas as colunas: institution, country e score
df.loc[:, ["institution", "country", "score"]]


# 2. Mostre universidades entre rank 50 e 100
df_rank_50_100 = df.loc[
    (df["world_rank"] >= 50) & (df["world_rank"] <= 100),
    ["institution", "world_rank", "country", "score"]
]
df_rank_50_100


# 3. Mostre universidades cujo país é “United Kingdom”
df_uk = df.loc[
    df["country"] == "United Kingdom",
    ["institution", "world_rank", "country", "score"]
]
df_uk

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# %%
# Exercício 5 – Valores Ausentes 

# 1. Quantos valores nulos existem na coluna broad_impact?
nulos = df["broad_impact"].isnull().sum()
nulos


# 2. Qual percentual do dataset é nulo?
percentual_nulo = (nulos / len(df)) * 100
percentual_nulo


# 3. Remova linhas com broad_impact nulo
df_sem_nulos = df.dropna(subset=["broad_impact"])
df_sem_nulos


# 4. Preencha valores nulos com a média
media_original = df["broad_impact"].mean()

df_preenchido = df.copy()
df_preenchido["broad_impact"] = df_preenchido["broad_impact"].fillna(media_original)

df_preenchido


# 5. Compare a média antes e depois do preenchimento
media_antes = df["broad_impact"].mean()
media_depois = df_preenchido["broad_impact"].mean()

media_antes, media_depois

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# %%
# Exercício 6 – Análise por País 

# 1. Média do score por país
media_por_pais = df.groupby("country")["score"].mean()
media_por_pais


# 2. País com maior média de score
pais_maior_media = media_por_pais.sort_values(ascending=False).head(1)
pais_maior_media


# 3. Quantidade de universidades por país
qtd_por_pais = df["country"].value_counts()
qtd_por_pais


# 4. Top 10 países com mais universidades
top10_paises = df["country"].value_counts().head(10)
top10_paises


# %%
# Exercício 7 – Análise por Ano 

import matplotlib.pyplot as plt

# 1. Média do score por ano
media_por_ano = df.groupby("year")["score"].mean()
media_por_ano


# 2. Qual ano teve maior média?
ano_maior_media = media_por_ano.idxmax()
maior_media = media_por_ano.max()

ano_maior_media, maior_media


# 3. Gráfico da evolução do score médio ao longo do tempo
# %%
