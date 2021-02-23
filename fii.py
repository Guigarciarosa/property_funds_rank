#%%
import os
from bs4 import BeautifulSoup
from numpy.lib.shape_base import column_stack
import pandas as pd 
import requests
# %%
url = 'https://www.fundsexplorer.com.br/ranking'
response = requests.get(url)
# %%
soup = BeautifulSoup(response.text, 'html.parser')
# %%
data = []
table = soup.find(id="table-ranking") 
table_head = table.find('thead')
rows = table_head.find_all('tr')
for row in rows:
    cols = row.find_all('th')
    colsd = [ele.get_text(separator=" ").strip() for ele in cols]
    data.append([ele for ele in colsd])
# %%
table_body = table.find('tbody')
#%%
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    colsd = [ele.text.replace('R$','').replace('%','').replace('.0','').replace('.','').replace('N/A','').replace(',','.').strip() for ele in cols]
    data.append([ele for ele in colsd])
# %%
for x in data : df = pd.DataFrame(data=data)
# %%
df.columns = df.iloc[0]
# %%
df = df.drop(index=0)
# %%
import datetime
hoje = datetime.date.today()
# %%
import sqlite3
#%%
conn = sqlite3.connect('database_fii.db')
#%%
agora = datetime.datetime.now()
df['Hoje'] = agora
#%%
df = df.rename(columns={'Código do fundo':'codigo_do_fundo', 'Setor':'setor', 'Preço Atual':'preco_atual', 'Liquidez Diária':'liquidez_diaria',
       'Dividendo':'dividendo', 'Dividend Yield':'dividend_yield', 'DY (3M) Acumulado':'dy_3m_acumulado', 'DY (6M) Acumulado':'dy_6m_acumulado',
       'DY (12M) Acumulado':'DY_(12M)_Acumulado', 'DY (3M) Média':'dy_3m_media', 'DY (6M) Média':'dy_6m_media',
       'DY (12M) Média':'dy_12M_media', 'DY Ano':'dy_ano', 'Variação Preço':'variacao_preco', 'Rentab. Período':'rentabilidade_periodo',
       'Rentab. Acumulada':'rentabilidade_acumulada', 'Patrimônio Líq.':'patrimonio_liq', 'VPA':'vpa', 'P/VPA':'p_vpa',
       'DY Patrimonial':'dy_patrimonial', 'Variação Patrimonial':'variacao_patrimonial', 'Rentab. Patr. no Período':'rentabilidade_patrimonial_periodo',
       'Rentab. Patr. Acumulada':'rentabilidade_patrimonial_acumulada', 'Vacância Física':'vacancia_fisica', 'Vacância Financeira':'vacancia_financeira',
       'Quantidade Ativos':'quantidade_ativos', 'Hoje':'hoje'})
#%%
df.to_sql('ranking_diario', con=conn, index=False, if_exists='append')
# %%
conn.commit()
print("Conexão encerrada com database_fii", conn.close())

# %%
