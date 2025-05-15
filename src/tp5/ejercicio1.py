#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento
#* Chain of Responsibility
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

#* Clase base para todos los manejadores de la cadena

class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, number):
        raise NotImplementedError("Este método debe ser implementado por subclases")


#* Manejador que consume números pares

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} fue consumido por EvenHandler (par)")
        elif self.next:
            self.next.handle(number)
        else:
            print(f"{number} no fue consumido")


#* Manejador que consume números primos

class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} fue consumido por PrimeHandler (primo)")
        elif self.next:
            self.next.handle(number)
        else:
            print(f"{number} no fue consumido")


#* Manejador por defecto que marca el número como no consumido

class DefaultHandler(Handler):
    def handle(self, number):
        print(f"{number} no fue consumido por ningún handler")


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')

    print("\n--- Ejecución de cadena de responsabilidad ---\n")

    #*--- Se arma la cadena: primero primos, luego pares, luego default
    handler_chain = PrimeHandler(EvenHandler(DefaultHandler()))

    #*--- Se recorren los números del 1 al 100
    for i in range(1, 101):
        handler_chain.handle(i)

