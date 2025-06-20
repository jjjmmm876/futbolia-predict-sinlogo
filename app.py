import streamlit as st
import pandas as pd

st.set_page_config(page_title="FutbolIA Predict", page_icon="⚽", layout="centered")

st.title("⚽ FutbolIA Predict")
st.markdown("Bienvenido a tu app de predicciones de fútbol con IA.")

# Leer datos de ejemplo
df_partidos = pd.read_csv("data/partidos.csv")

# Seleccionar equipos
equipos = sorted(set(df_partidos['local']).union(set(df_partidos['visitante'])))
equipo_local = st.selectbox("Selecciona el equipo local", equipos)
equipo_visitante = st.selectbox("Selecciona el equipo visitante", equipos)

if equipo_local == equipo_visitante:
    st.warning("Selecciona dos equipos diferentes.")
else:
    if st.button("Predecir resultado"):
        datos = df_partidos[
            (df_partidos['local'] == equipo_local) &
            (df_partidos['visitante'] == equipo_visitante)
        ]

        if datos.empty:
            st.info("No hay historial entre estos equipos. Predicción basada en promedio.")
            local_prom = df_partidos[df_partidos['local'] == equipo_local]['goles_local'].mean()
            visit_prom = df_partidos[df_partidos['visitante'] == equipo_visitante]['goles_visitante'].mean()
        else:
            local_prom = datos['goles_local'].mean()
            visit_prom = datos['goles_visitante'].mean()

        st.success(f"Predicción simulada: **{equipo_local} {round(local_prom)} - {round(visit_prom)} {equipo_visitante}**")
