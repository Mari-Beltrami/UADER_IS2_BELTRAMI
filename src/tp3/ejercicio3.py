from abc import ABC, abstractmethod

#clase abstracta
class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self):
        pass

#clases concretas
class EntregaMostrador(Hamburguesa):
    def entregar(self):
        print("La hamburguesa se entrega en mostrador.")

class EntregaRetiroCliente(Hamburguesa):
    def entregar(self):
        print("El cliente retira la hamburguesa.")

class EntregaDelivery(Hamburguesa):
    def entregar(self):
        print("La hamburguesa será enviada por delivery.")

#Fábrica
class HamburguesaFactory:
    @staticmethod
    def crear_entrega(tipo):
        if tipo == "mostrador":
            return EntregaMostrador()
        elif tipo == "retiro":
            return EntregaRetiroCliente()
        elif tipo == "delivery":
            return EntregaDelivery()
        else:
            raise ValueError("Tipo de entrega no válido.")

#Prueba
entrega1 = HamburguesaFactory.crear_entrega("mostrador")
entrega2 = HamburguesaFactory.crear_entrega("retiro")
entrega3 = HamburguesaFactory.crear_entrega("delivery")

entrega1.entregar()
entrega2.entregar()
entrega3.entregar()

