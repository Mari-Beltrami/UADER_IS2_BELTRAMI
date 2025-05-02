#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Bridge
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

class TrenLaminador:
    '''Implementador - interfaz común para los trenes laminadores'''

    def producir(self):
        '''Método que debe implementar cada tren concreto'''
        pass


class TrenLaminador5m(TrenLaminador):
    '''Tren laminador que genera planchas de 5 metros'''

    def producir(self):
        print("Produciendo lámina de 5 metros de largo...")


class TrenLaminador10m(TrenLaminador):
    '''Tren laminador que genera planchas de 10 metros'''

    def producir(self):
        print("Produciendo lámina de 10 metros de largo...")


class Lamina:
    '''Abstracción que representa una lámina genérica'''

    def __init__(self, implementador: TrenLaminador):
        self.tren = implementador
        self.espesor = 0.5  # pulgadas
        self.ancho = 1.5    # metros

    def producir(self):
        print(f"\nLámina: {self.espesor}\" espesor - {self.ancho} m de ancho")
        self.tren.producir()


"""main method"""

if __name__ == "__main__":

    import os
    os.system('clear')  # En Windows usar 'cls'

#*--- Creamos láminas con diferentes trenes laminadores

    tren_5m = TrenLaminador5m()
    tren_10m = TrenLaminador10m()

    lamina1 = Lamina(tren_5m)
    lamina2 = Lamina(tren_10m)

    # Producción con tren de 5 mts
    lamina1.producir()

    # Producción con tren de 10 mts
    lamina2.producir()

