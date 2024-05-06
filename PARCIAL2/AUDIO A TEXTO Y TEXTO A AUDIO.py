import speech_recognition as sr
from gtts import gTTS
import os

def audio_a_texto(nombre_archivo):
    r = sr.Recognizer()
    with sr.AudioFile(nombre_archivo) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='es-ES')
        return text

def texto_a_audio(texto, nombre_archivo_salida):
    tts = gTTS(text=texto, lang='es')
    tts.save(nombre_archivo_salida)
    os.system("start " + nombre_archivo_salida)  # Reproduce el archivo de audio

# Nombre del archivo de audio de entrada
archivo_audio_entrada = "audio.wav"

# Convertir audio a texto
texto_obtenido = audio_a_texto(archivo_audio_entrada)
print("Texto obtenido del audio:", texto_obtenido)

# Convertir texto a audio y reproducirlo
archivo_audio_salida = "texto_convertido.mp3"
texto_a_audio(texto_obtenido, archivo_audio_salida)
