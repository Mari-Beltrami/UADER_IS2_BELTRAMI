"""Una situación representativa donde es útil aplicar el patrón Flyweight es en el desarrollo de un editor de texto o procesador de palabras, como por ejemplo Microsoft Word, Google Docs o Notepad.

En este tipo de aplicaciones, cada documento puede contener miles o millones de caracteres. Si se generara una instancia de objeto por cada carácter (letra, número o símbolo), la utilización de memoria sería extremadamente ineficiente. Sin embargo, muchos de estos caracteres comparten características como el tipo de letra (fuente), el tamaño, y el estilo. Aquí es donde se vuelve ideal el uso del patrón Flyweight."""

"""En este ejercicio se implementa una clase Letra que encapsula el estado compartido (caracter, fuente, tamaño), y una fábrica FabricaLetras que se encarga de crear las instancias necesarias solo si no existían previamente. Si ya existe un objeto Letra('a', 'Arial', 12), este se reutiliza, sin crear uno nuevo.

A través de esta estrategia, si un documento contiene miles de letras “a” en Arial 12, todas compartirán la misma instancia, y solo cambiarán sus coordenadas (estado externo). De esta manera se logra una drástica reducción del consumo de memoria, especialmente en contextos con muchos elementos repetitivos."""

#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Flyweight
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

class Letra:
    '''Flyweight - representa el estado interno compartido de una letra'''

    def __init__(self, caracter, fuente, tamaño):
        self.caracter = caracter
        self.fuente = fuente
        self.tamaño = tamaño

    def mostrar(self, fila, columna):
        '''Usa estado externo (posición) junto con el interno (caracter)'''
        print(f"Letra '{self.caracter}' en posición ({fila}, {columna}) - Fuente: {self.fuente}, Tamaño: {self.tamaño}")


class FabricaLetras:
    '''Fábrica de flyweights - reutiliza objetos Letra ya existentes'''

    _letras = {}

    @classmethod
    def obtener_letra(cls, caracter, fuente, tamaño):
        clave = (caracter, fuente, tamaño)
        if clave not in cls._letras:
            cls._letras[clave] = Letra(caracter, fuente, tamaño)
        return cls._letras[clave]


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')  # En Windows usar 'cls'

#*--- Usamos la fábrica para reutilizar letras

    texto = [
        ('H', 0, 0), ('o', 0, 1), ('l', 0, 2), ('a', 0, 3),
        ('H', 1, 0), ('o', 1, 1), ('l', 1, 2), ('a', 1, 3)
    ]

    for caracter, fila, columna in texto:
        letra = FabricaLetras.obtener_letra(caracter, "Arial", 12)
        letra.mostrar(fila, columna)

#*--- Verificamos que se reutilizaron objetos
    print(f"\nCantidad de objetos letra creados: {len(FabricaLetras._letras)}")

