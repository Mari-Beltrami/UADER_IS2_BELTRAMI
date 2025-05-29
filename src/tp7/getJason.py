#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* TP7 - Ingeniería Reversa, Re-factoría y Re-Ingeniería
#* getJason.py - Versión final refactorizada y robusta
#* Copyright UADER-FCyT-IS2 ©2024 todos los derechos reservados
#*
#* Funcionalidad:
#*   Recupera el valor de una clave dentro de 'sitedata.json'.
#*   Usa 'token1' por defecto si no se pasa ninguna clave.
#*   Implementa el patrón Singleton para asegurar una única instancia.
#*   Controla errores para evitar fallas no controladas.
#*   Permite elegir entre versión vieja y versión nueva usando branching.
#*   Muestra versión con argumento '-v'.
#*
#* Ejemplo de uso:
#*   python3 getJason.py               → imprime el valor de 'token1'
#*   python3 getJason.py token2        → imprime el valor de 'token2'
#*   python3 getJason.py -v            → muestra la versión del programa
#*
#*------------------------------------------------------------------------

import json
import sys
import os

# Flag para activar la nueva versión refactorizada
USE_NEW_VERSION = True  # ← cambiar a False para usar la versión vieja

# ---------------------------
# Versión Antigua (Legacy)
# ---------------------------
def legacy_version():
    jsonfile = 'sitedata.json'
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            print("getJason.py versión 1.1")
            sys.exit(0)
        jsonkey = sys.argv[1]
    else:
        jsonkey = 'token1'
    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        if jsonkey in obj:
            print(str(obj[jsonkey]))
        else:
            print(f"Error: La clave '{jsonkey}' no existe en el archivo.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Error: El archivo {jsonfile} no existe.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)

# ---------------------------
# Versión Nueva (Refactorizada, Singleton, robusta)
# ---------------------------
class TokenReader:
    """Singleton para manejar lectura del archivo sitedata.json"""
    _instance = None

    @staticmethod
    def get_instance():
        """Devuelve la única instancia existente"""
        if TokenReader._instance is None:
            TokenReader()
        return TokenReader._instance

    def __init__(self):
        if TokenReader._instance is not None:
            raise Exception("Esta clase es un Singleton. Usa get_instance().")
        TokenReader._instance = self
        self.jsonfile = 'sitedata.json'
        self.data = {}
        self.load_data()

    def load_data(self):
        """Carga y parsea el archivo JSON"""
        if not os.path.exists(self.jsonfile):
            print(f"Error: El archivo {self.jsonfile} no existe.")
            sys.exit(1)
        try:
            with open(self.jsonfile, 'r') as file:
                self.data = json.load(file)
        except json.JSONDecodeError:
            print("Error: El archivo JSON está mal formado.")
            sys.exit(1)

    def get_token(self, key):
        """Devuelve el valor asociado a la clave"""
        if key in self.data:
            return self.data[key]
        print(f"Error: La clave '{key}' no existe en el archivo.")
        sys.exit(1)

def new_version():
    """Versión refactorizada usando Singleton"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            print("getJason.py versión 1.1")
            sys.exit(0)
        jsonkey = sys.argv[1]
    else:
        jsonkey = 'token1'

    try:
        reader = TokenReader.get_instance()
        value = reader.get_token(jsonkey)
        print(value)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)

# ---------------------------
# Punto de entrada principal
# ---------------------------
def main():
    """Controlador principal que decide qué versión usar"""
    if USE_NEW_VERSION:
        new_version()
    else:
        legacy_version()

if __name__ == "__main__":
    main()

