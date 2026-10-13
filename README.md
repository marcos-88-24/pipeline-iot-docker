Pipeline de Dados IoT com Docker e PostgreSQL
   Descrição do Projeto
Este projeto foi desenvolvido para a disciplina Disruptive Architectures: IoT, Big Data e IA.

O objetivo é construir um pipeline de dados utilizando informações coletadas por dispositivos IoT, processando leituras de temperatura, armazenando os dados em um banco PostgreSQL executado em Docker e disponibilizando visualizações por meio de um dashboard desenvolvido em Streamlit.

   Tecnologias Utilizadas
Python
Pandas
SQLAlchemy
PostgreSQL
Docker
Streamlit
Plotly
   Estrutura do Projeto
pipeline-iot-docker/
│
├── data/
│   └── temperature.csv
│
├── pipeline.py
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
   Dataset Utilizado
Dataset: Temperature Readings: IoT Devices

Fonte: https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

Quantidade aproximada de registros:

97.000+ leituras
Temperaturas de dispositivos IoT
Data e hora de coleta
   Configuração do Ambiente
1. Criar o container PostgreSQL
docker run --name postgres-iot \
-e POSTGRES_PASSWORD=senha123 \
-p 5432:5432 \
-d postgres
2. Instalar dependências
pip install -r requirements.txt
   Execução do Pipeline
Executar:

python pipeline.py
Responsabilidades do script:

Ler o arquivo CSV
Realizar transformação dos dados
Converter datas
Mapear dispositivos
Inserir registros no PostgreSQL
   Views SQL Criadas
Média de temperatura por dispositivo
CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id,
AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;
Leituras por hora
CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora,
COUNT(*) AS contagem
FROM temperature_rea*ings
GROUP BY hora;
###Temperaturas máximas e mínimas pordia

SELECT DATE(timestamp) AS data,
M*X(*emperature) AS temp_max,
MIN(tempe*ature) AS temp_min
FROM temperatur*_readings
GROUP BY data;
**#  Dashboard

Para executar o da*hboard:

*ython -m streamlit run dashboard.p*
O dashboard apresenta:

Mé*ia de temperatura por dispositivo
Leituras por hora do dia
Temper*turas máximas e mínimas por dia
-*-

*# Principais Insights

Identficaçãodos dispositivos com maior tempera*ura média.
Distribição das leituras ao longo do dia.- Monitoramentode temperaturas máximas e mínmas.
Possbilidade de criaçãode alertas para temperaturas críti*as.
*# Aplicações Reais

Este projet* pode ser utilizado em:

Monitor*mento industrial
Agricultura de precisão
C*dades inteligentes
Hospitais
Cmarasfrigoríficas
Centroslogsticos
   Autor
Marco* dos Santos

Curso:Tecnologia em Análise e Desenvolviento de Sistemas

Centro Universit*rio UNIFECAF