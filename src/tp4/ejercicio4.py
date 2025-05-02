#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Decorator
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

class Numero:
    '''Clase base que representa el número original'''

    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Valor: {self.valor}")
        return self.valor


class Decorador:
    '''Clase base para decoradores'''

    def __init__(self, componente):
        self.componente = componente

    def mostrar(self):
        return self.componente.mostrar()


class Sumar2(Decorador):
    '''Decorator que suma 2 al resultado'''

    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor + 2
        print(f" +2 → {resultado}")
        return resultado


class Multiplicar2(Decorador):
    '''Decorator que multiplica por 2'''

    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor * 2
        print(f" *2 → {resultado}")
        return resultado


class Dividir3(Decorador):
    '''Decorator que divide por 3'''

    def mostrar(self):
        valor = self.componente.mostrar()
        resultado = valor / 3
        print(f" /3 → {resultado}")
        return resultado


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')  # En Windows usar 'cls'

#*--- Número base

    print("Número original sin decoradores:")
    n = Numero(9)
    n.mostrar()

#*--- Decoradores aplicados individualmente

    print("\nAplicando decoradores por separado:")

    s = Sumar2(n)
    s.mostrar()

    m = Multiplicar2(n)
    m.mostrar()

    d = Dividir3(n)
    d.mostrar()

#*--- Decoradores anidados

    print("\nAplicando decoradores anidados (sumar + multiplicar + dividir):")
    resultado_final = Dividir3(Multiplicar2(Sumar2(n)))
    resultado_final.mostrar()

