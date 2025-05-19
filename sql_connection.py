import sqlalchemy as sql
import senhas
from data_collecting import df_completo, df_municipios, df_regioes, df_uf

# URL da conexão usando pymysql
db_url = f"mysql+pymysql://{senhas.user}:{senhas.password}@{senhas.host}:{senhas.port}/{senhas.database}"

# Cria engine e testa conexão
engine = sql.create_engine(db_url)

# Testa to_sql
df_completo.to_sql('localidades', engine, if_exists='replace', index=False)
df_municipios.to_sql('municipios', engine, if_exists='replace', index=False)
df_regioes.to_sql('regioes', engine, if_exists='replace', index=False)
df_uf.to_sql('uf', engine, if_exists='replace', index=False)


print("Tabela criada com sucesso.")