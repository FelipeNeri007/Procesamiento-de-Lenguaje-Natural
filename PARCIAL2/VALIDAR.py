import os

def validar_nombre_documento(nombre_documento):
    """
    Función para validar si el documento de Word existe.
    """
    if os.path.exists(nombre_documento):
        return True
    else:
        return False

def capturar_nombre_documento():
    """
    Función para capturar el nombre del documento de Word.
    """
    nombre_documento = input("Introduce el nombre del documento de Word: ")
    return nombre_documento

def main():
    """
    Función principal del programa.
    """
    while True:
        nombre_documento = capturar_nombre_documento()
        if validar_nombre_documento(nombre_documento):
            print("El documento existe.")
            break
        else:
            print("El documento no existe. Por favor, ingresa otro nombre de documento.")

if __name__ == "__main__":
    main()
