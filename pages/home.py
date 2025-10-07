import streamlit as st

st.title('Boxeo Stats App 🥊')

st.header('¡Bienvenido a mi comparador de boxeadores leyenda!')

st.info('Selecciona una opción en el navegador de la barra lateral')

if st.button("🎯 Ver estadísticas ahora"):
    st.switch_page("pages/estadisticas.py")

st.image('https://res.cloudinary.com/usopc-prod/image/upload/v1735249906/NGB%20Boxing/2024%20in%20Photos/Wednesday_10.30.24_-_59.jpg', width=600)