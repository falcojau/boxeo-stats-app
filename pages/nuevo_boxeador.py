import streamlit as st

st.title('🥊 Añade Nuevo Boxeador')

# 1. Definir el diálogo 
@st.dialog('Boxeador añadido')
def boxeador_añadido(nombre):
    st.write(f'{nombre} ha sido añadido con éxito. ✅')
    if st.button("Cerrar"):
        st.rerun()

# 2. Se almacena en st.session_state
if "boxeadores" not in st.session_state:
    st.session_state.boxeadores = []

# 3. Crear formulario
with st.form('mi_form'):
    # Definir variables de los inputs
    nombre_boxeador = st.text_input('Nombre y Apellidos del Boxeador')
    victorias = st.number_input('Victorias', min_value=0)
    derrotas = st.number_input('Derrotas', min_value=0)
    kos = st.number_input("KO's", min_value=0)
    
    submitted = st.form_submit_button('Añadir')
# 3.1. Aviso de error o éxito si ha introducido un boxeador o no
if submitted:
    if nombre_boxeador.strip() == "":
        st.warning('Por favor, introduce un nombre válido ⚠️​')
    else:
        # 3.2. Si el usuario envia un boxeador correctamente...
        st.session_state.boxeadores.append({
            "Nombre": nombre_boxeador,
            "Victorias": victorias,
            "Derrotas": derrotas,
            "KOs": kos
        })
        boxeador_añadido(nombre_boxeador)

# 4. Mostramos los boxeadores añadidos hasta el momento
if st.session_state.boxeadores:
    st.subheader("📋 Boxeadores añadidos:")
    st.dataframe(st.session_state.boxeadores)