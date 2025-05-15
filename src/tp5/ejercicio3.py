#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento
#* Observer
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

#* Clase que actúa como publicador y gestiona a los observers

class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def emit(self, id_emitido):
        print(f"\n[Publisher] Emitiendo ID: {id_emitido}")
        for observer in self.subscribers:
            observer.notify(id_emitido)


#* Clase base para los observers

class Observer:
    def __init__(self, id_personal):
        self.id_personal = id_personal

    def notify(self, id_emitido):
        raise NotImplementedError("Subclase debe implementar este método")


#* Observador concreto que reacciona cuando coincide su ID

class ConcreteObserver(Observer):
    def notify(self, id_emitido):
        if self.id_personal == id_emitido:
            print(f"→ {self.id_personal} detectado: Acción realizada por Observer")


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')

    print("\n--- Patrón Observer con IDs ---\n")

    #*--- Crear publisher
    radio = Publisher()

    #*--- Crear observers con distintos IDs
    obs1 = ConcreteObserver("A123")
    obs2 = ConcreteObserver("B456")
    obs3 = ConcreteObserver("C789")
    obs4 = ConcreteObserver("D321")

    #*--- Registrar suscripciones
    radio.subscribe(obs1)
    radio.subscribe(obs2)
    radio.subscribe(obs3)
    radio.subscribe(obs4)

    #*--- Emitir 8 IDs (al menos 4 deben coincidir)
    ids_a_emitir = ["X999", "A123", "Z000", "B456", "Y111", "C789", "W222", "D321"]

    for id_em in ids_a_emitir:
        radio.emit(id_em)

    print("\n")

