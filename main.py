import streamlit as st

st.set_page_config(
    page_title='Boxeo Stats App 🥊',
    page_icon='🥊',
    layout="wide",
    initial_sidebar_state='auto'
)

# Barra Lateral
home = st.Page('pages/home.py', title='🏡 Home')
estadisticas = st.Page('pages/estadisticas.py', title='📊​ Estadisticas')
nuevo_boxeador = st.Page('pages/nuevo_boxeador.py', title='🥊 Añade Nuevo Boxeador')
about = st.Page('pages/acerca_de.py', title='🖋️​ Acerca de mi')

pg = st.navigation([home, estadisticas, nuevo_boxeador, about])
pg.run()