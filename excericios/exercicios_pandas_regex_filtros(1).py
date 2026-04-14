"""
Aula - Exercicios de Filtros Regex com Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados com print.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Regex ajuda a filtrar texto com padroes.
- Resolva um exercicio por vez.
"""

import pandas as pd
arquivo = "cadastro_alunos.xlsx"
df = pd.read_excel(arquivo)
# ---------------------------------------------
# EXERCICIO 1
# ---------------------------------------------
"""
Filtre nomes que começam com a letra A
"""
# RESOLUCAO
filtro = df ["nome_aluno"] == "DANILO SODRÉ BARCELOS"
df.loc[filtro, :]

filtro = df ["nome_aluno"].str.contains("A")
df.loc[filtro, :]
# ---------------------------------------------
# EXERCICIO 2
# ---------------------------------------------
"""
Filtre nomes que terminam com "Silva"
"""
# RESOLUCAO
Filtro = df ["nome_aluno"].str.contains("Barcelos" , case=False)
df.loc[filtro, :]


# ---------------------------------------------
# EXERCICIO 3
# ---------------------------------------------
"""
Filtre nomes que começam com M
"""
# RESOLUCAO
filtro = df ["nome_aluno"].str.contains("M")
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 4
# ---------------------------------------------
"""
Filtre nomes que começam com:
A ou B ou C
"""

filtro = df ["nome_aluno"].str.contains(r"^[ABC]")
df.loc[filtro, :]

# Dica regex
# r"^[ABC]"
# RESOLUCAO


# ---------------------------------------------
# EXERCICIO 5
# ---------------------------------------------
"""
Filtre nomes que começam com:
Ana OU Maria
"""
# Dica
# r"^(Ana|Maria)"
# RESOLUCAO

filtro = df ["nome_aluno"].str.contains(r"^(Ana|Maria)", case=False)
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 6
# ---------------------------------------------
"""
Filtre nomes que possuem a palavra "Paulo"
em qualquer posição
"""
# RESOLUCAO
filtro = df ["nome_aluno"].str.contains("Paulo", case=False)
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 7
# ---------------------------------------------
"""
Filtre nomes com exatamente dois nomes
Exemplo:
Ana Souza
Bruno Lima
"""
# Dica
# r"^[A-Za-z]+ [A-Za-z]+$"
# RESOLUCAO

filtro = df ["nome_aluno"].str.contains(r"^[A-Za-z]+ [A-Za-z]+$", case=False)
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 8
# ---------------------------------------------
"""
Filtre nomes com três palavras
"""
# RESOLUCAO
filtro = df["nome_aluno"].astype(str).str.contains(r"^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$", case=False)
df.loc[filtro, :]
# ---------------------------------------------
# EXERCICIO 9
# ---------------------------------------------
"""
Filtre nomes que tenham Santos OU Silva
"""
# RESOLUCAO
filtro = df["nome_aluno"].astype(str).str.contains(r"^(?:Santos|Silva)", case=False)
df.loc[filtro , :]

# ---------------------------------------------
# EXERCICIO 10
# ---------------------------------------------
"""
Filtre nomes que terminam com:
Costa ou Alves
"""
# RESOLUCAO
filtro = df["nome_aluno"].astype(str).str.contains(r"^(?:Costa|Alves)$", case=False)
df.loc[filtro , :]

# ---------------------------------------------
# EXERCICIO 11
# ---------------------------------------------
"""
Filtre nomes que possuem apenas letras e espaços
(remover empresas)
"""
# Dica
# r"^[A-Za-z ]+$"
# RESOLUCAO
filtro = df ["nome_aluno"].str.contains(r"^[A-Za-z ]+$")
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 12
# ---------------------------------------------
"""
Filtre nomes que começam com letra maiuscula
"""
# Dica
# r"^[A-Z]"
# RESOLUCAO
filtro = df ["nome_aluno"].str.contains(r"^[A-Z]")
df.loc[filtro, :]


# ---------------------------------------------
# EXERCICIO 13
# ---------------------------------------------
"""
Filtre nomes que possuem "Maria" ignorando maiúsculas/minúsculas
"""
filtro = df["nome_aluno"].str.contains("Maria", case=False)
df.loc[filtro, :]
# Dica
# case=False
# RESOLUCAO


# ---------------------------------------------
# EXERCICIO 14
# ---------------------------------------------

"""
Filtre nomes que possuem duas palavras
e terminam com Souza ou Lima ou Rocha
"""
filtro = df["nome_aluno"].str.contains(r"^\w+\s(?:Souza|Lima|Rocha)$", case=False)
df.loc[filtro, :]
# RESOLUCAO




dados_clientes = {
    "cliente": [
        "Ana Souza",
        "Bruno Lima",
        "Carla Mendes",
        "Daniel Rocha",
        "Empresa XPTO Ltda",
        "Mercado Bom Preco",
    ],
    "email": [
        "ana.souza@gmail.com",
        "bruno_lima@empresa.com.br",
        "carla.mendes@yahoo.com",
        "daniel@outlook.com",
        "contato@xpto.com.br",
        "vendas@bompreco.com.br",
    ],
    "cidade": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Sao Paulo", "Curitiba"],
    "codigo_cliente": ["CLI-001", "CLI-002", "VIP-101", "CLI-003", "EMP-501", "VIP-102"],
}
df_clientes = pd.DataFrame(dados_clientes)

# Exercicio 15:
# Filtre os registros onde:
# a) email termina com ".com.br"
# b) cliente contem a palavra "Mercado"
# c) codigo_cliente comeca com "VIP"
#
# Dica:
# Use str.contains com padroes regex:
# - r"\.com\.br$"
# - r"Mercado"
# - r"^VIP"

# RESOLUCAO: complete aqui
# a
filtro = df_clientes["email"].str.contains(r"\.com\.br$", case=False)
df_clientes.loc[filtro]

# b
filtro = df_clientes["cliente"].str.contains("Mercado", case=False)
df_clientes.loc[filtro]

# c
filtro = df_clientes["codigo_cliente"].str.contains(r"^VIP", case=False)
df_clientes.loc[filtro]
# Exercicio 16:
# Filtre os clientes cujo codigo esteja no formato:
# 3 letras maiusculas + "-" + 3 digitos
# Exemplo valido: CLI-001
#
# Dica de regex:
# r"^[A-Z]{3}-\d{3}$"

# RESOLUCAO: complete aqui



# Exercicio 17:
# Encontre emails que sejam de:
# - gmail.com OU outlook.com
#
# Dica de regex:
# r"@(gmail|outlook)\.com$"

# RESOLUCAO: complete aqui
# Exercicio 17
df_clientes = pd.DataFrame(dados_clientes)
filtro = df_clientes["email"].str.contains(r"@(gmail|outlook)\.com$", case=False, na=False)
df_clientes.loc[filtro]


# Inclui valores com caixa diferente e um valor ausente.
df_leads = pd.DataFrame(
    {
        "origem": ["Instagram", "instagram", "LinkedIn", "EMAIL", None, "Google Ads"],
        "campanha": ["Promo Verao", "promo verao", "B2B_Q1", "BLACK_FRIDAY", "Teste", "Leads_2026"],
    }
)

# Exercicio 18:
# a) Filtre origem contendo "instagram" sem diferenciar maiusculas/minusculas
# b) Filtre campanhas que tenham apenas letras, espacos e underscore
# c) Garanta que valores nulos nao quebrem o filtro
#
# Dicas:
# - case=False
# - na=False
# - regex sugerida para (b): r"^[A-Za-z_ ]+$"

# RESOLUCAO: complete aqui
df_leads = pd.DataFrame(
    {
        "origem": ["Instagram", "instagram", "LinkedIn", "EMAIL", None, "Google Ads"],
        "campanha": ["Promo Verao", "promo verao", "B2B_Q1", "BLACK_FRIDAY", "Teste", "Leads_2026"],
    }
)
# a)
filtro = df_leads["origem"].str.contains("instagram", case=False, na=False)
df_leads.loc[filtro]

# b)
filtro = df_leads["campanha"].str.contains(r"^[A-Za-z_ ]+$", na=False)
df_leads.loc[filtro]

# c)
# o na=False já foi usado acima para não quebrar com valores nulos



import pandas as pd
import requests


# ============================================================
# CONFIGURAÇÕES
# ============================================================
CSV_PATH = "ncr_ride_bookings.csv"   # ajuste o caminho se necessário
TOKEN = "SEU_JWT"                    # substitua pelo seu token
BASE_URL = "https://laboratoriodefinancas.com/api/v2"

# ============================================================
# QUESTÕES 1 a 6 — Dataset NCR Ride Bookings
# ============================================================
df = pd.read_csv(ncr_ride_bookings.csv)

# Q1 — Corridas com status "Completed"
completed = df[df["Booking Status"] == "Completed"]
q1 = len(completed)
print(f"Q1 – Corridas Completed: {q1}")

# Q2 — Proporção em relação ao total
q2 = q1 / len(df)
print(f"Q2 – Proporção Completed: {q2:.4f}  ({q2*100:.2f}%)")

# Q3 — Média da distância por tipo de veículo
q3 = df.groupby("Vehicle Type")["Ride Distance"].mean().round(2)
print("\nQ3 – Média de Ride Distance por Vehicle Type:")
print(q3.to_string())

# Q4 — Método de pagamento mais usado por Bikes
bikes = df[df["Vehicle Type"] == "Bike"]
q4 = bikes["Payment Method"].value_counts().idxmax()
print(f"\nQ4 – Payment Method mais usado por Bike: {q4}")

# Q5 — Valor total arrecadado nas corridas Completed
q5 = completed["Booking Value"].sum()
print(f"\nQ5 – Total Booking Value (Completed): {q5:,.2f}")

# Q6 — Ticket médio das corridas Completed
q6 = completed["Booking Value"].mean()
print(f"Q6 – Ticket médio (Completed): {q6:.2f}")

# ============================================================
# QUESTÃO 7 — API IPEA: metadados FIPE — vendas de imóveis Brasil
# ============================================================
print("\n--- Q7/Q8: IPEA ---")
url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_meta = requests.get(url_meta)
meta = pd.DataFrame(resp_meta.json()["value"])

# Filtra FIPE + vendas de imóveis no Brasil
fipe = meta[meta["FNTSIGLA"] == "FIPE"]
vendas = fipe[fipe["SERNOME"].str.contains("vendas", case=False, na=False)]
vendas_br = vendas[vendas["SERNOME"].str.contains("Brasil", case=False, na=False)]
print("\nQ7 – Séries FIPE relacionadas a vendas de imóveis no Brasil:")
print(vendas_br[["SERCODIGO", "SERNOME"]].to_string(index=False))

# ============================================================
# QUESTÃO 8 — Valores da série encontrada; data e valor máximo
# ============================================================
if not vendas_br.empty:
    codigo = vendas_br["SERCODIGO"].iloc[0]
    print(f"\nQ8 – SERCODIGO encontrado: {codigo}")

    url_vals = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')"
    resp_vals = requests.get(url_vals)
    vals = pd.DataFrame(resp_vals.json()["value"])[["VALDATA", "VALVALOR"]]
    vals["VALVALOR"] = pd.to_numeric(vals["VALVALOR"], errors="coerce")

    idx_max = vals["VALVALOR"].idxmax()
    print(f"Q8 – Data do valor máximo : {vals.loc[idx_max, 'VALDATA']}")
    print(f"Q8 – Valor máximo         : {vals.loc[idx_max, 'VALVALOR']}")
else:
    print("Q8 – Nenhuma série encontrada com os filtros aplicados.")

# ============================================================
# QUESTÃO 9 — Rendimento da VALE3 em 2025
# ============================================================
print("\n--- Q9: VALE3 2025 ---")
params_vale = {
    "ticker": "VALE3",
    "data_ini": "2001-01-01",
    "data_fim": "2026-12-31",
}
resp_vale = requests.get(
    f"{BASE_URL}/preco/corrigido",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params=params_vale,
)
vale_df = pd.DataFrame(resp_vale.json()["value"])
vale_df["data"] = pd.to_datetime(vale_df["data"])
vale_2025 = vale_df[vale_df["data"].dt.year == 2025].copy()

preco_inicio = vale_2025.sort_values("data")["preco_corrigido"].iloc[0]
preco_fim    = vale_2025.sort_values("data")["preco_corrigido"].iloc[-1]
rendimento   = (preco_fim / preco_inicio - 1) * 100
print(f"Q9 – Preço início 2025 : {preco_inicio:.2f}")
print(f"Q9 – Preço fim 2025    : {preco_fim:.2f}")
print(f"Q9 – Rendimento 2025   : {rendimento:.2f}%")

# ============================================================
# QUESTÃO 10 — Empresa de tecnologia com maior ROE em 2024-04-01
# ============================================================
print("\n--- Q10: Planilhão 2024-04-01 ---")
resp_plan = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params={"data_base": "2024-04-01"},
)
plan_df = pd.DataFrame(resp_plan.json()["value"])

tech = plan_df[plan_df["setor"].str.lower() == "tecnologia"].copy()
tech["roe"] = pd.to_numeric(tech["roe"], errors="coerce")
maior_roe = tech.loc[tech["roe"].idxmax(), ["ticker", "setor", "roe"]]
print("Q10 – Empresa de tecnologia com maior ROE:")
print(maior_roe.to_frame().T.to_string(index=False))

# ============================================================
# QUESTÕES 11 e 12 — Magic Formula (ROC + EY) — carteira de 10 ações
# ============================================================
print("\n--- Q11/Q12: Magic Formula ---")
resp_mf = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params={"data_base": "2024-04-01"},
)
mf_df = pd.DataFrame(resp_mf.json()["value"])

# Converte indicadores e remove NaN
mf_df["roc"] = pd.to_numeric(mf_df["roc"], errors="coerce")
mf_df["ey"]  = pd.to_numeric(mf_df["ey"],  errors="coerce")
mf_df = mf_df.dropna(subset=["roc", "ey"])

# Ranking: menor posição = melhor; ordena descendente e atribui rank (1 = melhor)
mf_df["rank_roc"] = mf_df["roc"].rank(ascending=False)
mf_df["rank_ey"]  = mf_df["ey"].rank(ascending=False)
mf_df["rank_total"] = mf_df["rank_roc"] + mf_df["rank_ey"]

carteira = mf_df.nsmallest(10, "rank_total")[["ticker", "setor", "roc", "ey", "rank_total"]]
print("Q11 – Carteira Magic Formula (10 ações):")
print(carteira.to_string(index=False))

# Q12 — Quantos setores na carteira
q12 = carteira["setor"].nunique()
print(f"\nQ12 – Número de setores distintos na carteira: {q12}")
print("Setores:", carteira["setor"].unique().tolist())







import pandas as pd
import requests

# ============================================================
# CONFIGURAÇÕES
# ============================================================
CSV_PATH = "ncr_ride_bookings.csv"   # ajuste o caminho se necessário
BASE_URL  = "https://laboratoriodefinancas.com/api/v2"
TOKEN     = "SEU_JWT_AQUI"           # substitua pelo seu token

# ============================================================
# CARREGA O DATASET
# ============================================================
df = pd.read_csv(CSV_PATH)

# ============================================================
# Q1 – Corridas com status "Completed"
# ============================================================
completed = df[df["Booking Status"] == "Completed"]
q1 = len(completed)
print(f"\nQ1 – Corridas Completed: {q1}")

# ============================================================
# Q2 – Proporção em relação ao total
# ============================================================
q2 = q1 / len(df) * 100
print(f"Q2 – Proporção: {q2:.2f}%  ({q1}/{len(df)})")

# ============================================================
# Q3 – Média de Ride Distance por Vehicle Type
# ============================================================
q3 = df.groupby("Vehicle Type")["Ride Distance"].mean().round(2)
print("\nQ3 – Média de distância por tipo de veículo:")
print(q3.to_string())

# ============================================================
# Q4 – Método de pagamento mais usado em Bike
# ============================================================
bike = df[df["Vehicle Type"] == "Bike"]
q4 = bike["Payment Method"].value_counts()
print("\nQ4 – Métodos de pagamento (Bike):")
print(q4.to_string())
print(f"     -> Mais usado: {q4.idxmax()}")

# ============================================================
# Q5 – Valor total arrecadado (Completed)
# ============================================================
q5 = completed["Booking Value"].sum()
print(f"\nQ5 – Valor total Completed: {q5:,.2f}")

# ============================================================
# Q6 – Ticket médio (Completed)
# ============================================================
q6 = completed["Booking Value"].mean()
print(f"Q6 – Ticket médio Completed: {q6:.2f}")

# ============================================================
# Q7 – Séries FIPE relacionadas a vendas de imóveis no Brasil
# ============================================================
print("\n--- Q7/Q8: IPEA ---")
url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_meta = requests.get(url_meta)
meta = pd.DataFrame(resp_meta.json()["value"])

fipe      = meta[meta["FNTSIGLA"] == "FIPE"]
vendas    = fipe[fipe["SERNOME"].str.contains("vendas", case=False, na=False)]
vendas_br = vendas[vendas["SERNOME"].str.contains("Brasil", case=False, na=False)]
print("\nQ7 – Séries FIPE relacionadas a vendas de imóveis no Brasil:")
print(vendas_br[["SERCODIGO", "SERNOME"]].to_string(index=False))

# ============================================================
# Q8 – Data e valor máximo da série encontrada
# ============================================================
if not vendas_br.empty:
    codigo = vendas_br["SERCODIGO"].iloc[0]
    print(f"\nQ8 – SERCODIGO encontrado: {codigo}")

    url_vals  = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')"
    resp_vals = requests.get(url_vals)
    vals      = pd.DataFrame(resp_vals.json()["value"])[["VALDATA", "VALVALOR"]]
    vals["VALVALOR"] = pd.to_numeric(vals["VALVALOR"], errors="coerce")

    idx_max = vals["VALVALOR"].idxmax()
    print(f"Q8 – Data do valor máximo : {vals.loc[idx_max, 'VALDATA']}")
    print(f"Q8 – Valor máximo         : {vals.loc[idx_max, 'VALVALOR']}")
else:
    print("Q8 – Nenhuma série encontrada com os filtros aplicados.")

# ============================================================
# Q9 – Rendimento da VALE3 em 2025
# ============================================================

print("\n--- Q9: VALE3 2025 ---")
params_vale = {
    "ticker"  : "VALE3",
    "data_ini": "2001-01-01",
    "data_fim": "2026-12-31",
}
resp_vale = requests.get(
    f"{BASE_URL}/preco/corrigido",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params=params_vale,
)
vale_df       = pd.DataFrame(resp_vale.json()["value"])
vale_df["data"] = pd.to_datetime(vale_df["data"])
vale_2025     = vale_df[vale_df["data"].dt.year == 2025].sort_values("data")

preco_inicio = vale_2025["preco_corrigido"].iloc[0]
preco_fim    = vale_2025["preco_corrigido"].iloc[-1]
rendimento   = (preco_fim / preco_inicio - 1) * 100
print(f"Q9 – Preço início 2025 : {preco_inicio:.2f}")
print(f"Q9 – Preço fim 2025    : {preco_fim:.2f}")
print(f"Q9 – Rendimento 2025   : {rendimento:.2f}%")

# ============================================================
# Q10 – Empresa de tecnologia com maior ROE (data_base 2024-04-01)
# ============================================================
print("\n--- Q10: Maior ROE – Tecnologia ---")
resp_plan = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params={"data_base": "2024-04-01"},
)
plan_df = pd.DataFrame(resp_plan.json()["value"])

tech    = plan_df[
    (plan_df["setor"].str.lower() == "tecnologia") &
    (plan_df["data_base"] == "2024-04-01")
].copy()
tech["roe"] = pd.to_numeric(tech["roe"], errors="coerce")
top_roe = tech.nlargest(1, "roe")[["ticker", "setor", "roe"]]
print(top_roe.to_string(index=False))

# ============================================================
# Q11 – Magic Formula (ROC + EY) – carteira de 10 ações (2024-04-01)
# ============================================================
print("\n--- Q11: Magic Formula ---")
mf = plan_df[plan_df["data_base"] == "2024-04-01"].copy()
mf["roc"] = pd.to_numeric(mf["roc"], errors="coerce")
mf["ey"]  = pd.to_numeric(mf["ey"],  errors="coerce")
mf = mf.dropna(subset=["roc", "ey"])

mf["rank_roc"] = mf["roc"].rank(ascending=False)
mf["rank_ey"]  = mf["ey"].rank(ascending=False)
mf["magic"]    = mf["rank_roc"] + mf["rank_ey"]

carteira = mf.nsmallest(10, "magic")[["ticker", "setor", "roc", "ey", "magic"]].reset_index(drop=True)
carteira.index += 1
print(carteira.to_string())

# ============================================================
# Q12 – Quantos setores distintos na carteira?
# ============================================================
q12 = carteira["setor"].nunique()
print(f"\nQ12 – Setores distintos na carteira: {q12}")
print(carteira["setor"].value_counts().to_string())




import pandas as pd
import requests

CSV_PATH = "ncr_ride_bookings.csv"  # ajuste o caminho se necessário

df = pd.read_csv(CSV_PATH)

# ── Q1 ──────────────────────────────────────────────────────────────────────
completed = df[df["Booking Status"] == "Completed"]
q1 = len(completed)
print(f"\nQ1 – Corridas Completed: {q1}")

# ── Q2 ──────────────────────────────────────────────────────────────────────
q2 = q1 / len(df) * 100
print(f"Q2 – Proporção: {q2:.2f}%  ({q1}/{len(df)})")

# ── Q3 ──────────────────────────────────────────────────────────────────────
q3 = df.groupby("Vehicle Type")["Ride Distance"].mean().round(2)
print("\nQ3 – Média de distância por tipo de veículo:")
print(q3.to_string())

# ── Q4 ──────────────────────────────────────────────────────────────────────
bike = df[df["Vehicle Type"] == "Bike"]
q4 = bike["Payment Method"].value_counts()
print(f"\nQ4 – Método mais usado (Bike): {q4.idxmax()} ({q4.max()} usos)")

# ── Q5 ──────────────────────────────────────────────────────────────────────
q5 = completed["Booking Value"].sum()
print(f"\nQ5 – Valor total Completed: {q5:,.2f}")

# ── Q6 ──────────────────────────────────────────────────────────────────────
q6 = completed["Booking Value"].mean()
print(f"Q6 – Ticket médio Completed: {q6:.2f}")

# ── Q7 / Q8 – IPEA ──────────────────────────────────────────────────────────
print("\n--- Q7/Q8: IPEA ---")
url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_meta = requests.get(url_meta, timeout=60)
meta = pd.DataFrame(resp_meta.json()["value"])

fipe = meta[meta["FNTSIGLA"] == "FIPE"]
vendas_br = fipe[
    fipe["SERNOME"].str.contains("vendas", case=False, na=False) &
    fipe["SERNOME"].str.contains("Brasil", case=False, na=False)
]
print("Q7 – Séries FIPE vendas Brasil:")
print(vendas_br[["SERCODIGO", "SERNOME"]].to_string(index=False))

if not vendas_br.empty:
    codigo = vendas_br["SERCODIGO"].iloc[0]
    print(f"\nQ8 – SERCODIGO: {codigo}")
    url_vals = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')"
    resp_vals = requests.get(url_vals, timeout=60)
    vals = pd.DataFrame(resp_vals.json()["value"])[["VALDATA", "VALVALOR"]]
    vals["VALVALOR"] = pd.to_numeric(vals["VALVALOR"], errors="coerce")
    idx_max = vals["VALVALOR"].idxmax()
    print(f"Q8 – Data do valor máximo: {vals.loc[idx_max, 'VALDATA']}")
    print(f"Q8 – Valor máximo:         {vals.loc[idx_max, 'VALVALOR']}")

# ── Q9 – VALE3 2025 ─────────────────────────────────────────────────────────
print("\n--- Q9: VALE3 2025 ---")
BASE_URL = "https://laboratoriodefinancas.com/api/v2"
TOKEN = "SEU_JWT_AQUI"  # substitua pelo seu token
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

resp_vale = requests.get(
    f"{BASE_URL}/preco/corrigido",
    headers=HEADERS,
    params={"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"},
    timeout=30,
)
vale_df = pd.DataFrame(resp_vale.json()["value"])
vale_df["data"] = pd.to_datetime(vale_df["data"])
vale_2025 = vale_df[vale_df["data"].dt.year == 2025].sort_values("data")

preco_inicio = vale_2025["preco_corrigido"].iloc[0]
preco_fim    = vale_2025["preco_corrigido"].iloc[-1]
rendimento   = (preco_fim / preco_inicio - 1) * 100
print(f"Q9 – Preço início 2025: {preco_inicio:.2f}")
print(f"Q9 – Preço fim 2025:    {preco_fim:.2f}")
print(f"Q9 – Rendimento 2025:   {rendimento:.2f}%")

# ── Q10 – Tecnologia maior ROE ───────────────────────────────────────────────
print("\n--- Q10: Tecnologia maior ROE (2024-04-01) ---")
resp_plan = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers=HEADERS,
    params={"data_base": "2024-04-01"},
    timeout=30,
)
plan_df = pd.DataFrame(resp_plan.json()["value"])

tech = plan_df[plan_df["setor"].str.lower() == "tecnologia"]
maior_roe = tech.sort_values("roe", ascending=False).head(1)
print(maior_roe[["ticker", "setor", "roe"]].to_string(index=False))

# ── Q11 – Magic Formula ──────────────────────────────────────────────────────
print("\n--- Q11: Magic Formula (2024-04-01) ---")
mf = plan_df[["ticker", "setor", "roc", "ey"]].dropna(subset=["roc", "ey"])
mf = mf[(mf["roc"] > 0) & (mf["ey"] > 0)].copy()
mf["rank_roc"] = mf["roc"].rank(ascending=False)
mf["rank_ey"]  = mf["ey"].rank(ascending=False)
mf["rank_total"] = mf["rank_roc"] + mf["rank_ey"]
carteira = mf.sort_values("rank_total").head(10)
print(carteira[["ticker", "setor", "roc", "ey", "rank_total"]].to_string(index=False))

# ── Q12 – Setores da carteira ────────────────────────────────────────────────
print("\n--- Q12: Setores na carteira ---")
q12 = carteira["setor"].nunique()
print(f"Q12 – Número de setores: {q12}")
print(f"Setores: {carteira['setor'].unique().tolist()}")