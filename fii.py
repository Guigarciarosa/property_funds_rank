#%%
import os
from bs4 import BeautifulSoup
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
df.to_excel('fundos_imobiliarios_{}.xlsx'.format(hoje), index=False)
# %%
import sqlite3
#%%
conn = sqlite3.connect('database_fii.db')
#%%
agora = datetime.datetime.now()
df['Hoje'] = agora
#%%
df.to_sql('ranking_diario', con=conn, index=False, if_exists='append')
# %%
i
# %%
