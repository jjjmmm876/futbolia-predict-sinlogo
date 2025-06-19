import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="FutbolIA Predict", page_icon="⚽", layout="centered")

st.title("⚽ FutbolIA Predict")
st.markdown("Bienvenido a tu app de predicciones de fútbol con IA.")

# Cargar el modelo (simulación por ahora)
@st.cache_resource
def cargar_modelo():
    return joblib.load("models/modelo_random_forest.pkl")

modelo = cargar_modelo()

# Leer datos de ejemplo
df_partidos = pd.read_csv("data/partidos.csv")

# Seleccionar equipos para predicción
equipos = sorted(set(df_partidos['local']).union(set(df_partidos['visitante'])))
equipo_local = st.selectbox("Selecciona el equipo local", equipos)
equipo_visitante = st.selectbox("Selecciona el equipo visitante", equipos)

if equipo_local == equipo_visitante:
    st.warning("Selecciona dos equipos diferentes.")
else:
    if st.button("Predecir resultado"):
        # Simulación de predicción (puedes ajustar según tus variables reales)
        datos = df_partidos[
            (df_partidos['local'] == equipo_local) &
            (df_partidos['visitante'] == equipo_visitante)
        ]

        if datos.empty:
            st.info("No hay datos previos de este partido. Se usará predicción genérica.")
            X = pd.DataFrame([{
                'local_goles_prom': df_partidos[df_partidos['local'] == equipo_local]['goles_local'].mean(),
                'visit_goles_prom': df_partidos[df_partidos['visitante'] == equipo_visitante]['goles_visitante'].mean()
            }])
        else:
            X = datos[['local_goles_prom', 'visit_goles_prom']].iloc[0:1]

        pred = modelo.predict(X)[0]

        st.success(f"Predicción: **{equipo_local} {pred} - {equipo_visitante}**")
