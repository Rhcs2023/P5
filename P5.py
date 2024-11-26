import streamlit as st
import pyttsx3
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    'a': '1 ',
    'b': '2 ',
    'c': '3 ',
    'd': '4 ',
    'e': '5 ',
    'f': '6 ',
    'g': '7 ',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
    return oracion_traducida

def reproducir_audio(texto):
    # Inicializar el motor de pyttsx3
    engine = pyttsx3.init()
    
    # Configurar la voz (opcional)
    engine.setProperty('rate', 150)  # Velocidad de la voz
    engine.setProperty('volume', 1)  # Volumen (0.0 a 1.0)

    # Guardar el audio en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
        engine.save_to_file(texto, tmp.name)
        engine.runAndWait()
        with open(tmp.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    
    return audio_bytes

st.title("Traductor de palabras")

# Estado de la sesión para la traducción
if 'oracion_traducida' not in st.session_state:
    st.session_state.oracion_traducida = ""

# Opción para introducir texto
oracion_usuario = st.text_input("Introduce una oración para traducir:")

# Traducir la oración ingresada por el usuario
if oracion_usuario:
    oracion_traducida = traducir_oracion(oracion_usuario)
    st.session_state.oracion_traducida = oracion_traducida
    st.write(f"Traducción: {oracion_traducida}")
    audio_bytes = reproducir_audio(oracion_traducida)  # Usando pyttsx3
    st.audio(audio_bytes, format='audio/wav')