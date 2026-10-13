import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.title("Dashboard de Temperaturas IoT")

try:
    engine = create_engine(
        "postgresql://postgres:senha123@localhost:5432/postgres"
    )

    df_avg = pd.read_sql(
        "SELECT * FROM avg_temp_por_dispositivo",
        engine
    )

    st.header("Média de Temperatura por Dispositivo")
    st.dataframe(df_avg.head())
    st.plotly_chart(
        px.bar(df_avg, x="device_id", y="avg_temp")
    )

    df_hora = pd.read_sql(
        "SELECT * FROM leituras_por_hora",
        engine
    )

    st.header("Leituras por Hora")
    st.dataframe(df_hora.head())
    st.plotly_chart(
        px.line(df_hora, x="hora", y="contagem")
    )

    df_dia = pd.read_sql(
        "SELECT * FROM temp_max_min_por_dia",
        engine
    )

    st.header("Temperaturas Máximas e Mínimas por Dia")
    st.dataframe(df_dia.head())
    st.plotly_chart(
        px.line(
            df_dia,
            x="data",
            y=["temp_max", "temp_min"]
        )
    )

except Exception as e:
    st.error(f"Erro encontrado: {e}")