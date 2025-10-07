'''Un pequeño dataset (cacheado con @st.cache_data) con boxeadores y sus victorias, derrotas y KOs. ✅​
Gráficos interactivos (Plotly) para comparar.
Un formulario (st.form) para añadir un nuevo boxeador.
Un diálogo (st.dialog) que confirme cuando se añade correctamente.'''

import streamlit as st
import pandas as pd
import plotly.express as px

st.title('📊 ​Estadisticas')

# 1. Datos base
base_boxeadores = pd.DataFrame({
        "Nombre": ["Mike Tyson", "Muhammad Ali", "Canelo Álvarez", "Floyd Mayweather"],
        "Victorias": [50, 56, 60, 50],
        "Derrotas": [6, 5, 2, 0],
        "KOs": [44, 37, 39, 27]
})

# 2. Si hay nuevos boxeadores...
if "boxeadores" in st.session_state and len(st.session_state.boxeadores) > 0:
    nuevos = pd.DataFrame(st.session_state.boxeadores)
    datos_boxeadores = pd.concat([base_boxeadores, nuevos], ignore_index=True)
else:
    datos_boxeadores = base_boxeadores

# 3. Derretimos el DataFrame para que Plotly pueda agrupar las barras
datos_melted = datos_boxeadores.melt(
    id_vars="Nombre",
    value_vars=["Victorias", "Derrotas", "KOs"],
    var_name="Métrica",
    value_name="Valor"
)

# 4. Crear el gráfico de barras agrupadas
fig = px.bar(
    datos_melted,
    x="Nombre",
    y="Valor",
    color="Métrica",
    barmode="group", # Esto es lo que crea las barras agrupadas
    title="Comparación de Estadísticas Clave de Boxeadores Leyenda",
    color_discrete_sequence=px.colors.qualitative.Vivid
)

st.plotly_chart(fig, use_container_width=True)