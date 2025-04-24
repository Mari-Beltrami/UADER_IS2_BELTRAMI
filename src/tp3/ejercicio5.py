#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Builder extensión para TP 3
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------


#Clase producto
class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def mostrar(self):
        print("Avión construido:")
        print(f"  Cuerpo: {self.body}")
        print(f"  Turbinas: {', '.join(self.turbinas)}")
        print(f"  Alas: {', '.join(self.alas)}")
        print(f"  Tren de aterrizaje: {self.tren_aterrizaje}")

#Builder base
class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self, tipo="Estándar"):
        self.avion.body = tipo
        return self

    def construir_turbinas(self, cantidad=2, modelo="GE-Turbo"):
        self.avion.turbinas = [modelo for _ in range(cantidad)]
        return self

    def construir_alas(self, cantidad=2, tipo="Rectas"):
        self.avion.alas = [tipo for _ in range(cantidad)]
        return self

    def construir_tren_aterrizaje(self, tipo="Retráctil"):
        self.avion.tren_aterrizaje = tipo
        return self

    def build(self):
        return self.avion

#Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion_comercial(self):
        return (self.builder
                .construir_body("Avión Comercial")
                .construir_turbinas(2, "Rolls-Royce")
                .construir_alas(2, "Envergadura Extendida")
                .construir_tren_aterrizaje("Hidráulico")
                .build())

    def construir_avion_privado(self):
        return (self.builder
                .construir_body("Avión Privado")
                .construir_turbinas(2, "TurboFan Ligero")
                .construir_alas(2, "Delta")
                .construir_tren_aterrizaje("Fijo")
                .build())

#Uso del builder directamente
builder = AvionBuilder()
avion1 = (builder
          .construir_body("Avión Experimental")
          .construir_turbinas()
          .construir_alas()
          .construir_tren_aterrizaje()
          .build())
avion1.mostrar()

print("\n")

#uso del director para construir uno predefinido
director = Director(AvionBuilder())
avion2 = director.construir_avion_comercial()
avion2.mostrar()

