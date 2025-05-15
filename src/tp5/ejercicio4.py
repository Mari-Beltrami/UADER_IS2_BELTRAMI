#*--------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento
#* State con Frecuencias Memorizadas
#*--------------------------------------------------------------------

import os

#*-------- Clase base de todos los estados (AM, FM, Memorias)

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} ({})".format(self.stations[self.pos], self.name))


#*-------- Estado de AM

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def next(self):
        print("Cambiando a Memorias")
        self.radio.state = self.radio.memstate


#*-------- Estado de FM

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def next(self):
        print("Cambiando a Memorias")
        self.radio.state = self.radio.memstate


#*-------- Estado de Memorias

class MemoryState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["M1 (1250 AM)", "M2 (89.1 FM)", "M3 (1380 AM)", "M4 (103.9 FM)"]
        self.pos = 0
        self.name = "MEM"

    def next(self):
        # Alternar entre AM y FM luego de Memorias
        if isinstance(self.radio.state_previa, FmState):
            print("Cambiando a AM")
            self.radio.state = self.radio.amstate
        else:
            print("Cambiando a FM")
            self.radio.state = self.radio.fmstate

#*-------- Clase principal que orquesta los estados

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.memstate = MemoryState(self)

        self.state = self.fmstate
        self.state_previa = self.fmstate  # para alternar después de memorias

    def scan(self):
        self.state.scan()

    def next_mode(self):
        self.state_previa = self.state
        self.state.next()


#*-------- Ejecución

if __name__ == "__main__":
    os.system("clear")
    print("\nRadio con ciclo FM → MEM → AM → MEM...\n")

    radio = Radio()

    actions = [radio.scan] * 2 + [radio.next_mode]
    actions *= 6  # Repite el ciclo varias veces

    for action in actions:
        action()

