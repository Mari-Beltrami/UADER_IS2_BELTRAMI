#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* Calcula el factorial entre dos números usando programación orientada a objetos *
#*-------------------------------------------------------------------------*

class Factorial:
    #constructor: recibe el rango desde-hasta
    def __init__(self, minimo, maximo):
        self.min = minimo
        self.max = maximo

    #calcular factorial de un solo número
    def calcular(self, num):
        if num < 0:
            return f"{num}! = Error (negativo)"
        elif num == 0:
            return f"{num}! = 1"
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return f"{num}! = {fact}"

    #recorrer el rango y mostrar resultados
    def run(self):
        print(f"Calculando factoriales entre {self.min} y {self.max}")
        for i in range(self.min, self.max + 1):
            print(self.calcular(i))


#principal
if __name__ == "__main__":
    #ingreso de valores
    entrada = input("Ingrese un rango de la forma desde-hasta (ej. 4-8): ")

    if '-' in entrada:
        partes = entrada.split('-')
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            desde = int(partes[0])
            hasta = int(partes[1])

            #objeto Factorial
            f = Factorial(desde, hasta)
            f.run()
        else:
            print("Formato inválido. Usar: desde-hasta (ej. 3-6)")
    else:
        print("Entrada inválida. Debe contener un guion '-'")
