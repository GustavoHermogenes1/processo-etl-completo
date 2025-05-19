# %%
import requests
import json

url_uf = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

def get_response(url, **kwargs):
    resp = requests.get(url, params=kwargs)
    return resp.json()

uf = get_response(url_uf)

with open('uf.json', 'w', encoding='utf-8') as f:
    json.dump(uf, f, ensure_ascii='False', indent=4)
# %%
url_regioes = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes'

regioes = get_response(url_regioes)

with open('regioes.json', 'w', encoding='utf-8') as f:
    json.dump(regioes, f, ensure_ascii='False', indent=4)

# %%
url_municipios = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'

municipios = get_response(url_municipios)

with open('municipios.json', 'w', encoding='utf-8') as f:
    json.dump(municipios, f, ensure_ascii='False', indent=4)

# %%
import pandas as pd

# %%

df_uf = pd.DataFrame(uf, columns=['id', 'sigla', 'nome'])

df_uf.head()

# %%

df_regioes = pd.DataFrame(regioes, columns=['id', 'sigla', 'nome'])

df_regioes.head()

# %%

df_municipios = pd.DataFrame(municipios, columns=['id', 'nome'])

df_municipios.head()

# %%

ids_regiao = {}

for i in uf:
    ids_regiao[i['id']] = i['regiao']['id']

print(ids_regiao)

# %% 

df_uf.head()

# %%

df_uf['id_regiao'] = df_uf['id'].map(ids_regiao).fillna(0).astype('object')

df_uf.head()

# %%

df_uf['id_regiao'].describe()

# %%

df_uf['id_regiao'].unique()

# %% 

df_uf['id'] = df_uf['id'].astype('object')

df_uf.info()

# %%

df_municipios.head()

# %%

ids_ufs = {}

for i in municipios:
    try:
        ids_ufs[i['id']] = i['microrregiao']['mesorregiao']['UF']['id']
    except:
        ids_ufs[i['id']] = 'Nulo'

# %%

print(ids_ufs)

# %%

df_municipios['id_uf'] = df_municipios['id'].map(ids_ufs).astype('object')

df_municipios.head()

# %%

df_municipios['id_uf'].describe()

# %% 

df_municipios['id_uf'].unique()

# %% 

df_municipios[df_municipios['id_uf'] == 'Nulo']

# %% 

df_municipios['id_uf'].loc[5199] = 51

# %%

df_municipios.loc[5199]

# %% 

df_municipios['id_uf'].unique()

# %% 

df_municipios['id'] = df_municipios['id'].astype('object')

# %% 

df_municipios.info()

# %%

df_regioes.head()

# %%

df_regioes.info()

# %%

df_regioes['id'] = df_regioes['id'].astype('object')

# %%

df_uf.info()

# %%

df_uf['id'] = df_uf['id'].astype('object')

# %%
df_uf['nome'].unique()

# %%

df_uf.head()

# %%

df_municipios.head()

# %%

df_regioes.head()

# %%

df_completo = df_municipios.merge(df_uf, how='left', left_on='id_uf', right_on='id')

df_completo.head()

# %%

df_completo.drop(columns=['nome_x', 'id_y', 'sigla', 'nome_y'], inplace=True)

df_completo.head()

# %%

df_completo.rename(columns={
    'id_x' : 'id_municipio'
}, inplace=True)

df_completo.head()