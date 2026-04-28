import streamlit as st

import numpy as np

import pandas as pd

# Configuración de la página

st.set_page_config(page_title="Dashboard Ventas vs Costos", layout="wide")

st.title("📊 Dashboard de Ventas vs Costos")

# -------------------------

# Estado para regenerar datos

# -------------------------

if "data" not in st.session_state:

    st.session_state.data = None

# -------------------------

# Controles

# -------------------------

col1, col2 = st.columns(2)

with col1:

    n = st.slider("Cantidad de datos", 10, 200, 50)

with col2:

    if st.button("🔄 Generar nuevos datos"):

        ventas = np.random.randn(n)

        costos = np.random.randn(n)

        st.session_state.data = pd.DataFrame({

            "Ventas": ventas,

            "Costos": costos

        })

# Si no hay datos aún, generarlos automáticamente

if st.session_state.data is None:

    ventas = np.random.randn(n)

    costos = np.random.randn(n)

    st.session_state.data = pd.DataFrame({

        "Ventas": ventas,

        "Costos": costos

    })

df = st.session_state.data

# -------------------------

# Métricas

# -------------------------

col1, col2 = st.columns(2)

with col1:

    st.metric("Promedio Ventas", round(df["Ventas"].mean(), 2))

with col2:

    st.metric("Promedio Costos", round(df["Costos"].mean(), 2))

# -------------------------

# Comparación

# -------------------------

if df["Ventas"].mean() > df["Costos"].mean():

    st.success("📈 Las ventas son mayores que los costos")

else:

    st.error("📉 Los costos son mayores que las ventas")

# -------------------------

# Gráfica principal

# -------------------------

st.subheader("📉 Gráfica interactiva")

st.line_chart(df)

# -------------------------

# Tabla de datos

# -------------------------

with st.expander("Ver datos"):

    st.dataframe(df)

# -------------------------

# Extra: diferencia acumulada

# -------------------------

df["Diferencia"] = df["Ventas"] - df["Costos"]

st.subheader("📊 Diferencia Ventas - Costos")

st.bar_chart(df["Diferencia"])
