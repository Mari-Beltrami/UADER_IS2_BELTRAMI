#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* TP6 - Ingeniería Reversa, Refactorización y Re-Ingeniería
#* getJason.py - Versión corregida y documentada
#*
#* Funcionalidad:
#*   Este programa recupera el valor de una clave dentro de un archivo
#*   JSON llamado 'sitedata.json'. La clave se puede indicar como 
#*   argumento al ejecutar el script. Si no se indica ninguna, se utiliza 
#*   'token1' por defecto.
#*
#* Ejemplo de uso:
#*   python3 getJason.py          # imprime el valor de 'token1'
#*   python3 getJason.py token2   # imprime el valor de 'token2'
#*
#* Archivo JSON esperado:
#*   {
#*     "token1": "C598-ECF9-F0F7-881A",
#*     "token2": "C598-ECF9-F0F7-881B"
#*   }
#*
#* UADER - Ingeniería de Software II - Prof. Dr. Pedro E. Colla
#*------------------------------------------------------------------------

import json
import sys

# Archivo fijo que contiene las claves
jsonfile = 'sitedata.json'

# Si se pasa un argumento, se usa como clave; si no, se usa 'token1'
if len(sys.argv) > 1:
    jsonkey = sys.argv[1]
else:
    jsonkey = 'token1'

# Lectura del archivo JSON
with open(jsonfile, 'r') as myfile:
    data = myfile.read()

# Parseo del contenido JSON
obj = json.loads(data)

# Impresión del valor asociado a la clave
print(str(obj[jsonkey]))

