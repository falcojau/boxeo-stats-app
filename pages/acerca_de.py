import streamlit as st
import os
import pandas as pd

st.title('🖋️ ​Acerca de mi')

st.markdown("""
    Gracias por visitar mi primera página web, espero que te haya gustado el comparador de boxeadores leyenda.\n
    Soy Jaume Falcó Romanos, apasionado del **boxeo** y el **desarrollo de software**.  \n
    Esta app está hecha con 💪 y mucho `Streamlit`.\n
    ¡Hasta la próxima!            
""")

st.divider()

# Reseña
st.subheader("💭 Deja tu reseña sobre la web")

# 
if "reseñas" not in st.session_state:
    # Si ya existe un CSV, lo cargamos
    if os.path.exists("reseñas.csv"):
        st.session_state.reseñas = pd.read_csv("reseñas.csv").to_dict(orient="records")
    else:
        st.session_state.reseñas = []

nombre_reseñador = st.text_input('¿Cuál es tu nombre?')
calificacion = st.selectbox(
    '¿Qué puntuación le das a la web?',
    options=['Excelente (5/5)', 'Muy Buena (4/5)', 'Buena (3/5)', 'Regular (2/5)', 'Mala (1/5)'],
    index=0
)
comentario = st.text_area("Escribe un comentario opcional:", placeholder="¿Qué te ha parecido la app?")

# Acciones al pulsar el botón
if st.button('Enviar reseña 📤​'):
    nueva_reseña = {
        "Calificación": calificacion,
        "Comentario": comentario
    }

    # Añadimos a la lista y guardamos en CSV
    st.session_state.reseñas.append(nueva_reseña)
    df = pd.DataFrame(st.session_state.reseñas)
    df.to_csv("reseñas.csv", index=False)

    st.success(f'¡Muchas gracias {nombre_reseñador}! Seguiré trabajando para mejorar 👍​')
    st.toast(f'Has valorado la página web de Jaume con un {calificacion}')
    if comentario.strip():
        st.write('✍️​ Tu comentario:')
        st.info(comentario)
