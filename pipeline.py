import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:senha123@localhost:5432/postgres')

df = pd.read_csv('data/temperature.csv')

# Renomear colunas
df = df.rename(columns={
    'room_id/id': 'device_id',
    'noted_date': 'timestamp',
    'temp': 'temperature'
})

df = df[['device_id', 'timestamp', 'temperature']]

# Converter timestamp para datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', dayfirst=True)

# Mapear nomes para números
mapa = {nome: i+1 for i, nome in enumerate(df['device_id'].unique())}
df['device_id'] = df['device_id'].map(mapa)

# Inserir no banco
df.to_sql('temperature_readings', engine, if_exists='append', index=False)

print("Dados inseridos com sucesso!")
