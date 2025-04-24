class CalculadoraImpuestos:
    __instance = None  #Singleton

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls.__instance

    def calcular(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible no puede ser negativa")

        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contrib_municipal = base_imponible * 0.012

        total_impuestos = iva + iibb + contrib_municipal
        return total_impuestos


#Prueba del singleton y cálculo
c1 = CalculadoraImpuestos()
c2 = CalculadoraImpuestos()

print(c1 is c2)  #true: misma instancia

base = 1000
print(f"Impuestos sobre ${base}: ${c1.calcular(base):.2f}")  

