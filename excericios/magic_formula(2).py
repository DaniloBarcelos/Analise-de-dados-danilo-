# %%
# =============================================================
#  MAGIC FORMULA DE JOEL GREENBLATT — TOP 20 AÇÕES (B3)
#  Fonte de dados: Laboratório de Finanças (planilhão)
#  Lógica: rank(ROE) + rank(EV/EBIT) → menor rank = melhor
# =============================================================

import requests
import pandas as pd

# ----- CONFIGURAÇÃO -----
BASE_URL  = "https://laboratoriodefinancas.com/api/v2"
TOKEN     = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3NTQ4MDM0LCJpYXQiOjE3NzQ5NTYwMzQsImp0aSI6IjBiY2FkMWMyZTM0ZjQxOGZiZTMzNTNhNmIzZjg5Njc4IiwidXNlcl9pZCI6IjEwMSJ9.nnQMPvqhH5XTeZvs3x_yZmeN1kJ_eEyGvujlGI1T5t8"
DATA_BASE = "2026-03-28"
TOP_N     = 20

HEADERS = {"Authorization": f"Bearer {TOKEN}"}
kmk
# %%
# ----- 1. BUSCAR DADOS DO PLANILHÃO -----
resp = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers=HEADERS,
    params={"data_base": DATA_BASE},
)

if resp.status_code != 200:
    print(f"Erro na API: {resp.status_code} — {resp.text}")
else:
    print(f"✅ Dados recebidos! Status: {resp.status_code}")

dados = resp.json()
df = pd.DataFrame(dados)
print(f"Total de ações recebidas: {len(df)}")
print(f"Colunas disponíveis: {list(df.columns)}")

# %%
# ----- 2. MAGIC FORMULA (ROE + EV/EBIT) -----
# Colunas necessárias: ticker, roe, ev_ebit
colunas = ["ticker", "roe", "ev_ebit"]
df_mf = df[colunas].copy()

# Remover nulos e valores inválidos
df_mf = df_mf.dropna(subset=["roe", "ev_ebit"])

# EV/EBIT deve ser positivo (empresas com lucro operacional)
df_mf = df_mf[df_mf["ev_ebit"] > 0]

# ROE deve ser positivo (empresas lucrativas)
df_mf = df_mf[df_mf["roe"] > 0]

print(f"\nAções após filtros: {len(df_mf)}")

# ----- RANKINGS -----
# ROE: quanto MAIOR, melhor → rank decrescente (rank 1 = maior ROE)
df_mf["rank_roe"] = df_mf["roe"].rank(ascending=False)

# EV/EBIT: quanto MENOR, mais barata → rank crescente (rank 1 = menor EV/EBIT)
df_mf["rank_ev_ebit"] = df_mf["ev_ebit"].rank(ascending=True)

# Rank combinado (soma dos dois ranks — menor = melhor)
df_mf["rank_final"] = df_mf["rank_roe"] + df_mf["rank_ev_ebit"]

# Ordenar pelo rank final
df_mf = df_mf.sort_values("rank_final", ascending=True).reset_index(drop=True)
df_mf.index += 1  # posição começa em 1

# %%
# ----- 3. RESULTADO: TOP 20 -----
top20 = df_mf.head(TOP_N)[["ticker", "roe", "ev_ebit", "rank_roe", "rank_ev_ebit", "rank_final"]]

# Formatar para exibição
top20_fmt = top20.copy()
top20_fmt["roe"]      = top20_fmt["roe"].map(lambda x: f"{x:.2f}%")
top20_fmt["ev_ebit"]  = top20_fmt["ev_ebit"].map(lambda x: f"{x:.2f}x")
top20_fmt["rank_roe"]     = top20_fmt["rank_roe"].map(int)
top20_fmt["rank_ev_ebit"] = top20_fmt["rank_ev_ebit"].map(int)
top20_fmt["rank_final"]   = top20_fmt["rank_final"].map(int)

top20_fmt.columns = ["Ticker", "ROE", "EV/EBIT", "Rank ROE", "Rank EV/EBIT", "Rank Final"]

print(f"\n{'='*55}")
print(f"  MAGIC FORMULA — TOP {TOP_N} AÇÕES ({DATA_BASE})")
print(f"{'='*55}")
print(top20_fmt.to_string())
print(f"{'='*55}")
