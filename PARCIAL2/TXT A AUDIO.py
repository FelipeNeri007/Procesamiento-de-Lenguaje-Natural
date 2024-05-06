import pyttsx3

def text_to_speech(text):
    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()
    # Convertir el texto a voz
    engine.say(text)
    # Reproducir el audio
    engine.runAndWait()

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

def main():
    file_path = input("Introduce la ruta del archivo de texto (.txt): ")
    text = read_text_file(file_path)
    if text:
        text_to_speech(text)
    else:
        print("No se pudo convertir el texto a voz.")

if __name__ == "__main__":
    main()
