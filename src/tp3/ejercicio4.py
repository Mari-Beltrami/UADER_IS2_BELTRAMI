from abc import ABC, abstractmethod

#Clase abstracta
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def mostrar(self):
        pass

#Subclases concretas
class FacturaIVAResponsable(Factura):
    def mostrar(self):
        print(f"Factura A - Responsable Inscripto - Total: ${self.importe:.2f}")

class FacturaNoInscripto(Factura):
    def mostrar(self):
        print(f"Factura C - No Inscripto - Total: ${self.importe:.2f}")

class FacturaExento(Factura):
    def mostrar(self):
        print(f"Factura E - IVA Exento - Total: ${self.importe:.2f}")

#Fábrica
class FacturaFactory:
    @staticmethod
    def crear_factura(tipo_cliente, importe):
        if tipo_cliente == "responsable":
            return FacturaIVAResponsable(importe)
        elif tipo_cliente == "no_inscripto":
            return FacturaNoInscripto(importe)
        elif tipo_cliente == "exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Tipo de cliente no válido.")

#Prueba
f1 = FacturaFactory.crear_factura("responsable", 15000)
f2 = FacturaFactory.crear_factura("no_inscripto", 7800)
f3 = FacturaFactory.crear_factura("exento", 9800)

f1.mostrar()
f2.mostrar()
f3.mostrar()

