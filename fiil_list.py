#%%
import os
import pandas as pd 
from bs4 import BeautifulSoup
import requests
# %%
url = 'https://fiis.com.br/lupa-de-fiis'
response = requests.get(url)
# %%
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# %%
data = []
table = soup.find_all("div")
table
#%%


# %%
