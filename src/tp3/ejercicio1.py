class Factorial:
    __instance = None  #Variable de clase (privada) que guarda la instancia

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Factorial, cls).__new__(cls)
        return cls.__instance

    def calcular(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

#Prueba del singleton
f1 = Factorial()
f2 = Factorial()

print(f1 is f2)  #True: ambas variables apuntan a la misma instancia

#Uso del método
print(f1.calcular(5)) 
print(f2.calcular(3))

