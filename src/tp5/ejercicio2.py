#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento
#* Iterator
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

#* Clase que representa una colección de texto a recorrer

class TextCollection:
    def __init__(self, texto):
        self.texto = texto

    def get_forward_iterator(self):
        return ForwardIterator(self.texto)

    def get_reverse_iterator(self):
        return ReverseIterator(self.texto)


#* Iterador para recorrer la colección en orden directo

class ForwardIterator:
    def __init__(self, texto):
        self.texto = texto
        self.index = 0

    def has_next(self):
        return self.index < len(self.texto)

    def next(self):
        char = self.texto[self.index]
        self.index += 1
        return char


#* Iterador para recorrer la colección en orden inverso

class ReverseIterator:
    def __init__(self, texto):
        self.texto = texto
        self.index = len(texto) - 1

    def has_next(self):
        return self.index >= 0

    def next(self):
        char = self.texto[self.index]
        self.index -= 1
        return char


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')

    print("\n--- Patrón Iterator aplicado a una cadena de texto ---\n")

    texto = "Iteradores"
    coleccion = TextCollection(texto)

    print("Recorrido directo:")
    it_forward = coleccion.get_forward_iterator()
    while it_forward.has_next():
        print(it_forward.next(), end=" ")

    print("\n\nRecorrido inverso:")
    it_reverse = coleccion.get_reverse_iterator()
    while it_reverse.has_next():
        print(it_reverse.next(), end=" ")

    print("\n")

