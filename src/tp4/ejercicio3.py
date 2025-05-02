#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Composite
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

class Componente:
    '''Interfaz común para piezas y conjuntos'''

    def mostrar(self, nivel=0):
        pass


class Pieza(Componente):
    '''Componente hoja - no tiene hijos'''

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")


class SubConjunto(Componente):
    '''Componente compuesto - puede tener otros componentes (piezas o subconjuntos)'''

    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ SubConjunto: {self.nombre}")
        for comp in self.componentes:
            comp.mostrar(nivel + 1)


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')  # En Windows usar 'cls'

#*--- Creamos el producto principal (estructura jerárquica)

    producto = SubConjunto("Producto Principal")

    for i in range(1, 4):  # 3 subconjuntos iniciales
        sub = SubConjunto(f"SubConjunto {i}")
        for j in range(1, 5):  # Cada uno con 4 piezas
            sub.agregar(Pieza(f"Pieza {i}.{j}"))
        producto.agregar(sub)

#*--- Agregamos un subconjunto opcional con 4 piezas

    sub_opcional = SubConjunto("SubConjunto Opcional")
    for j in range(1, 5):
        sub_opcional.agregar(Pieza(f"Pieza O.{j}"))

    producto.agregar(sub_opcional)

#*--- Mostrar toda la estructura

    print("\nEstructura del ensamblado:")
    producto.mostrar()

