import streamlit as st

import numpy as np

import pandas as pd

# Título

st.title("📊 Dashboard de Ventas vs Costos")

# Slider

n = st.slider("Cantidad de datos", 10, 100, 50)

# Botón para regenerar datos

if "data" not in st.session_state:

    st.session_state.data = np.random.randn(n)

if st.button("🔄 Generar nuevos datos"):

    st.session_state.data = np.random.randn(n)

# Crear datos

x = np.arange(len(st.session_state.data))

ventas = st.session_state.data + np.random.randn(len(x)) * 0.5

costos = st.session_state.data

# DataFrame

df = pd.DataFrame({

    "Ventas": ventas,

    "Costos": costos

})

# Métricas

col1, col2 = st.columns(2)

col1.metric("Promedio Ventas", round(ventas.mean(), 2))

col2.metric("Promedio Costos", round(costos.mean(), 2))

# Gráfica

st.subheader("📈 Gráfica interactiva")

st.line_chart(df, use_container_width=True)

# Tabla opcional

if st.checkbox("Mostrar datos"):

    st.write(df)
min_val, max_val = st.slider(

    "Filtrar valores",

    float(df.min().min()),

    float(df.max().max()),

    (float(df.min().min()), float(df.max().max()))

)

df_filtrado = df[(df >= min_val) & (df <= max_val)]

st.subheader("📊 Datos filtrados")

st.line_chart(df_filtrado, use_container_width=True)
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(

    "📥 Descargar datos",

    csv,

    "datos.csv",

    "text/csv")

    if ventas.mean() > costos.mean():

    st.success("📈 Las ventas son mayores que los costos")

else:

    st.warning("⚠️ Los costos superan las ventas")

)
