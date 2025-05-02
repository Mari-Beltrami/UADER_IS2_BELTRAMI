#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones Estructurales
#* Proxy
#* UADER - Ingeniería de Software II
#*------------------------------------------------------------------------

import os

class Ping:
    '''Clase que representa el objeto real que hace el ping'''

    def execute(self, ip):
        '''Realiza 10 intentos de ping a la IP, solo si empieza con 192.'''
        print("\nEjecutando método 'execute' con validación de IP...")
        if ip.startswith("192."):
            print(f"IP válida ({ip}). Realizando 10 pings...")
            for i in range(10):
                os.system(f"ping -c 1 {ip}")  # Para Windows usar -n
        else:
            print(f"IP no permitida: {ip}. Solo se permite si comienza con '192.'")

    def executefree(self, ip):
        '''Realiza 10 intentos de ping a la IP sin validación'''
        print(f"\nEjecutando método 'executefree' sin validación de IP para: {ip}")
        for i in range(10):
            os.system(f"ping -c 1 {ip}")  # Para Windows usar -n


class PingProxy:
    '''Proxy que controla el acceso a Ping y redirige según condiciones'''

    def __init__(self):
        self.real_ping = Ping()

    def execute(self, ip):
        '''Controla el acceso según la IP, delega a Ping o redirige'''
        print("\nAcceso al Proxy. Evaluando IP ingresada...")

        if ip == "192.168.0.254":
            print("IP especial detectada. Redirigiendo ping a www.google.com (sin validación).")
            self.real_ping.executefree("www.google.com")
        else:
            print(f"Delegando ejecución normal para IP: {ip}")
            self.real_ping.execute(ip)


"""main method"""

if __name__ == "__main__":

    os.system('clear')  # En Windows: os.system('cls')

#*--- Instancia del proxy para ejecutar distintos casos

    ping_proxy = PingProxy()

    # Caso especial: redirige a www.google.com
    ping_proxy.execute("192.168.0.254")

    # Caso válido: IP comienza con 192., se permite
    ping_proxy.execute("192.168.1.123")

    # Caso inválido: IP no permitida, se bloquea
    ping_proxy.execute("8.8.8.8")

