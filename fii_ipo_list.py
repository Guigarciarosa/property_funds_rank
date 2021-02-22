#%%
import os
from bs4 import BeautifulSoup
import pandas as pd 
import requests
# %%
url = 'https://www.clubefii.com.br/fundo_imobiliario_lista'
response = requests.get(url)
# %%
soup = BeautifulSoup(response.text, 'html.parser')
#%%
data = []
table = soup.find(table)
print(table) 
#%%
table_head = table.find('thead')
rows = table_head.find_all('tr')
for row in rows:
    cols = row.find_all('th')
    colsd = [ele.get_text(separator=" ").strip() for ele in cols]
    data.append([ele for ele in colsd])
# %%
