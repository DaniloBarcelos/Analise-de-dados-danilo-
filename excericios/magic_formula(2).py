# %%
# =============================================================
#  MAGIC FORMULA DE JOEL GREENBLATT — TOP 20 AÇÕES (B3)
#  Fonte de dados: Laboratório de Finanças (planilhão)
#  Lógica: rank(ROE) + rank(P/EBIT) → menor rank = melhor
# =============================================================
import requests
import pandas as pd
from datetime import date, timedelta

# ----- CONFIGURAÇÃO -----
BASE_URL = "https://laboratoriodefinancas.com/api/v2"
TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NzAwNzE0LCJpYXQiOjE3NzYxMDg3MTQsImp0aSI6IjgwNTdmN2E2YWJmNTRkMTdhOTY4NjZlZDNkNTQ2MDNmIiwidXNlcl9pZCI6IjEwMSJ9.SS7-2EUIqHPqxMiwuHQzwb5AIjCyZTJRudUFkI0UoyU"
TOP_N    = 20
HEADERS  = {"Authorization": f"Bearer {TOKEN}"}

# %%
# ----- 1. BUSCAR DADOS -----
dados      = []
data_teste = date(2026, 4, 11)

for _ in range(10):
    resp = requests.get(
        f"{BASE_URL}/bolsa/planilhao",
        headers=HEADERS,
        params={"data_base": str(data_teste)},
    )
    if resp.status_code == 200:
        dados = resp.json()
        if len(dados) > 0:
            DATA_BASE = str(data_teste)
            print(f"✅ Dados encontrados para: {DATA_BASE} — {len(dados)} ações")
            break
        else:
            print(f"⚠️  Sem dados para {data_teste}, tentando dia anterior...")
    else:
        print(f"❌ Erro {resp.status_code} para {data_teste}")
    data_teste -= timedelta(days=1)

if not dados:
    raise RuntimeError("Nenhuma data com dados encontrada. Verifique o token.")

df = pd.DataFrame(dados)

# %%
# ----- 2. MAGIC FORMULA (ROE + P/EBIT) -----
df_mf = df[["ticker", "roe", "p_ebit"]].copy()

# Converter para número
df_mf["roe"]    = pd.to_numeric(df_mf["roe"], errors="coerce")
df_mf["p_ebit"] = pd.to_numeric(df_mf["p_ebit"], errors="coerce")

# Filtros
df_mf = df_mf.dropna(subset=["roe", "p_ebit"])
df_mf = df_mf[df_mf["p_ebit"] > 0]
df_mf = df_mf[df_mf["roe"] > 0]

print(f"Ações após filtros: {len(df_mf)}")

# Rankings
df_mf["rank_roe"]   = df_mf["roe"].rank(ascending=False)
df_mf["rank_pebit"] = df_mf["p_ebit"].rank(ascending=True)
df_mf["rank_final"] = df_mf["rank_roe"] + df_mf["rank_pebit"]

df_mf = df_mf.sort_values("rank_final").reset_index(drop=True)
df_mf.index += 1

# %%
# ----- 3. TOP 20 -----
top20 = df_mf.head(TOP_N)[["ticker", "roe", "p_ebit", "rank_roe", "rank_pebit", "rank_final"]].copy()

top20["roe"]        = top20["roe"].map(lambda x: f"{x:.2f}%")
top20["p_ebit"]     = top20["p_ebit"].map(lambda x: f"{x:.2f}x")
top20["rank_roe"]   = top20["rank_roe"].map(int)
top20["rank_pebit"] = top20["rank_pebit"].map(int)
top20["rank_final"] = top20["rank_final"].map(int)

top20.columns = ["Ticker", "ROE", "P/EBIT", "Rank ROE", "Rank P/EBIT", "Rank Final"]

print(f"\n{'='*60}")
print(f"  MAGIC FORMULA — TOP {TOP_N} AÇÕES  |  Data base: {DATA_BASE}")
print(f"{'='*60}")
print(top20.to_string())
print(f"{'='*60}")