# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:



import pandas as pd
import requests

CSV_PATH = "ncr_ride_bookings.csv"  

df = pd.read_csv(CSV_PATH)


# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
completed = df[df["Booking Status"] == "Completed"]
q1 = len(completed)
print(f"\nQ1 – Corridas Completed: {q1}")


# (0,5) 2 - Qual a proporção em relação ao total de corridas?

q2 = q1 / len(df) * 100
print(f"Q2 – Proporção: {q2:.2f}%  ({q1}/{len(df)})")

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.

q3 = df.groupby("Vehicle Type")["Ride Distance"].mean().round(2)
print("\nQ3 – Média de distância por tipo de veículo:")
print(q3.to_string())

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
bike = df[df["Vehicle Type"] == "Bike"]
q4 = bike["Payment Method"].value_counts()
print("\nQ4 – Métodos de pagamento (Bike):")
print(q4.to_string())
print(f"     -> Mais usado: {q4.idxmax()}")


# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
q5 = completed["Booking Value"].sum()
print(f"\nQ5 – Valor total Completed: {q5:,.2f}")

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?

q6 = completed["Booking Value"].mean()
print(f"Q6 – Ticket médio Completed: {q6:.2f}")

# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

print("\n--- Q7/Q8: IPEA ---")
url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp_meta = requests.get(url_meta)
meta = pd.DataFrame(resp_meta.json()["value"])


fipe = meta[meta["FNTSIGLA"] == "FIPE"]
vendas = fipe[fipe["SERNOME"].str.contains("vendas", case=False, na=False)]
vendas_br = vendas[vendas["SERNOME"].str.contains("Brasil", case=False, na=False)]
print("\nQ7 – Séries FIPE relacionadas a vendas de imóveis no Brasil:")
print(vendas_br[["SERCODIGO", "SERNOME"]].to_string(index=False))

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.
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



# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )








# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
import requests
import pandas as pd

BASE_URL = "https://laboratoriodefinancas.com/api/v2"
TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NzAwNzE0LCJpYXQiOjE3NzYxMDg3MTQsImp0aSI6IjgwNTdmN2E2YWJmNTRkMTdhOTY4NjZlZDNkNTQ2MDNmIiwidXNlcl9pZCI6IjEwMSJ9.SS7-2EUIqHPqxMiwuHQzwb5AIjCyZTJRudUFkI0UoyU"
HEADERS  = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(
    f"{BASE_URL}/bolsa/planilhao",
    headers=HEADERS,
    params={"data_base": "2024-04-01"},
)

df = pd.DataFrame(response.json())

df["roe"] = pd.to_numeric(df["roe"], errors="coerce")

tech = df[df["setor"].str.lower() == "tecnologia"]
maior_roe = tech.sort_values("roe", ascending=False).head(1)

print(maior_roe[["ticker", "setor", "roe"]].to_string(index=False))



# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
import requests
import pandas as pd
from datetime import date, timedelta

# ----- CONFIGURAÇÃO -----
BASE_URL = "https://laboratoriodefinancas.com/api/v2"
TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NzAwNzE0LCJpYXQiOjE3NzYxMDg3MTQsImp0aSI6IjgwNTdmN2E2YWJmNTRkMTdhOTY4NjZlZDNkNTQ2MDNmIiwidXNlcl9pZCI6IjEwMSJ9.SS7-2EUIqHPqxMiwuHQzwb5AIjCyZTJRudUFkI0UoyU"
TOP_N    = 10  # <-- alterado de 20 para 10
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
df_mf = df[["ticker", "setor", "roe", "p_ebit"]].copy()

df_mf["roe"]    = pd.to_numeric(df_mf["roe"], errors="coerce")
df_mf["p_ebit"] = pd.to_numeric(df_mf["p_ebit"], errors="coerce")

df_mf = df_mf.dropna(subset=["roe", "p_ebit"])
df_mf = df_mf[df_mf["p_ebit"] > 0]
df_mf = df_mf[df_mf["roe"] > 0]
print(f"Ações após filtros: {len(df_mf)}")

df_mf["rank_roe"]   = df_mf["roe"].rank(ascending=False)
df_mf["rank_pebit"] = df_mf["p_ebit"].rank(ascending=True)
df_mf["rank_final"] = df_mf["rank_roe"] + df_mf["rank_pebit"]
df_mf = df_mf.sort_values("rank_final").reset_index(drop=True)
df_mf.index += 1

# %%
# ----- 3. TOP 10 -----
top10 = df_mf.head(TOP_N)[["ticker", "setor", "roe", "p_ebit", "rank_roe", "rank_pebit", "rank_final"]].copy()
top10["roe"]        = top10["roe"].map(lambda x: f"{x:.2f}%")
top10["p_ebit"]     = top10["p_ebit"].map(lambda x: f"{x:.2f}x")
top10["rank_roe"]   = top10["rank_roe"].map(int)
top10["rank_pebit"] = top10["rank_pebit"].map(int)
top10["rank_final"] = top10["rank_final"].map(int)
top10.columns = ["Ticker", "Setor", "ROE", "P/EBIT", "Rank ROE", "Rank P/EBIT", "Rank Final"]

print(f"\n{'='*65}")
print(f"  MAGIC FORMULA — TOP {TOP_N} AÇÕES  |  Data base: {DATA_BASE}")
print(f"{'='*65}")
print(top10.to_string())
print(f"{'='*65}")

# %%
# ----- 4. Q12 – SETORES DA CARTEIRA -----
n_setores = top10["Setor"].nunique()
print(f"\nQ12 – Número de setores na carteira: {n_setores}")
print(f"Setores: {top10['Setor'].unique().tolist()}")




# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

n_setores = top10["Setor"].nunique()
print(f"Q12 – Número de setores na carteira: {n_setores}")
print(f"Setores: {top10['Setor'].unique().tolist()}")


