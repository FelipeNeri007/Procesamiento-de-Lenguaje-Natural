import requests
from bs4 import BeautifulSoup
import re

def buscar_palabra(url, palabra):
    # Obtener el contenido de la página web
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el texto de la página
        texto = soup.get_text()
        
        # Buscar la palabra específica en el texto
        ocurrencias = re.findall(r'\b' + palabra.lower() + r'\b', texto.lower())
        num_ocurrencias = len(ocurrencias)
        
        if num_ocurrencias > 0:
            print(f"La palabra '{palabra}' fue encontrada {num_ocurrencias} veces en la página {url}.")
        else:
            print(f"La palabra '{palabra}' no fue encontrada en la página {url}.")
    else:
        print("No se pudo obtener el contenido de la página.")

# URL de la página web a analizar
url = "https://www.coursera.org/mx/articles/what-is-python-used-for-a-beginners-guide-to-using-python"
# Palabra a buscar en la página
palabra_a_buscar = "python"

# Llamar a la función para buscar la palabra en la página
buscar_palabra(url, palabra_a_buscar)