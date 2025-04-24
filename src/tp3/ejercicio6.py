import copy

#clase base con soporte de clonación
class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

#clase concreta que hereda de Prototipo
class Documento(Prototipo):
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def mostrar(self):
        print(f"Título: {self.titulo}")
        print(f"Contenido: {self.contenido}")

#Prueba
original = Documento("Factura Prototipo", "Este es el contenido original.")
clon1 = original.clonar()
clon2 = clon1.clonar()

#cambiamos algo en clon2 para demostrar independencia
clon2.titulo = "Factura Clonada x2"

#mostrar resultados
print("Documento original:")
original.mostrar()

print("Primer clon:")
clon1.mostrar()

print("Segundo clon (a partir del primero):")
clon2.mostrar()

