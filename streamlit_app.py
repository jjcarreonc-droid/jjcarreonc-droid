import streamlit as st

import pandas as pd

import numpy as np

st.title("📊 Gráfica interactiva")

# Slider para controlar datos

n = st.slider("Cantidad de datos", 10, 100, 50)

data = pd.DataFrame(

    np.random.randn(n, 2),

    columns=["Ventas", "Costos"]

)

st.line_chart(data)
