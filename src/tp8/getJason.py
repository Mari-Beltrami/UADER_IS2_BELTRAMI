#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* TP8 - Ingeniería Reversa, Re-factoría y Re-Ingeniería
#* get_jason.py - Versión 1.2 final
#* Copyright UADER-FCyT-IS2 ©2024 todos los derechos reservados
#*
#* Descripción:
#* Automatiza la selección del banco para procesar pagos, balanceando cuentas.
#* Incluye Singleton para lectura de tokens, Chain of Responsibility para pagos,
#* Iterator para listar pagos, y manejo robusto de errores.
#*------------------------------------------------------------------------

import json
import sys
import os

VERSION = "1.2"

class TokenReader:
    """Singleton para manejar lectura del archivo sitedata.json"""
    _instance = None

    @staticmethod
    def get_instance():
        """Devuelve la única instancia existente"""
        if TokenReader._instance is None:
            TokenReader()
        return TokenReader._instance

    def __init__(self):
        """Inicializa el Singleton y carga datos"""
        if TokenReader._instance is not None:
            raise Exception("Esta clase es un Singleton. Usa get_instance().")
        TokenReader._instance = self
        self.jsonfile = 'sitedata.json'
        self.data = {}
        self.load_data()

    def load_data(self):
        """Carga y parsea el archivo JSON"""
        if not os.path.exists(self.jsonfile):
            print(f"Error: El archivo {self.jsonfile} no existe.")
            sys.exit(1)
        try:
            with open(self.jsonfile, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except json.JSONDecodeError:
            print("Error: El archivo JSON está mal formado.")
            sys.exit(1)

    def get_token(self, key):
        """Devuelve el valor asociado a la clave"""
        if key in self.data:
            return self.data[key]
        print(f"Error: La clave '{key}' no existe en el archivo.")
        sys.exit(1)

class AccountHandler:
    """Clase para manejar pagos entre cuentas"""
    def __init__(self, name, balance, token):
        """Inicializa cuenta con saldo y token"""
        self.name = name
        self.balance = balance
        self.token = token
        self.next_handler = None

    def set_next(self, handler):
        """Define el siguiente handler en la cadena"""
        self.next_handler = handler

    def handle_payment(self, order_number, amount):
        """Intenta procesar el pago o pasa al siguiente handler"""
        if self.balance >= amount:
            self.balance -= amount
            payment_record = {
                'pedido': order_number,
                'token': self.token,
                'monto': amount
            }
            PaymentsLog.get_instance().add_payment(payment_record)
            print(f"Pedido {order_number}: Pagado ${amount} usando {self.token}")
        elif self.next_handler:
            self.next_handler.handle_payment(order_number, amount)
        else:
            print(f"Pedido {order_number}: Fondos insuficientes en todas las cuentas.")

class PaymentsLog:
    """Singleton para registrar pagos realizados"""
    _instance = None

    @staticmethod
    def get_instance():
        """Devuelve la única instancia existente"""
        if PaymentsLog._instance is None:
            PaymentsLog()
        return PaymentsLog._instance

    def __init__(self):
        """Inicializa la lista de pagos"""
        if PaymentsLog._instance is not None:
            raise Exception("Esta clase es un Singleton. Usa get_instance().")
        PaymentsLog._instance = self
        self.payments = []

    def add_payment(self, payment):
        """Agrega un pago al registro"""
        self.payments.append(payment)

    def __iter__(self):
        """Devuelve un iterador sobre los pagos"""
        return iter(self.payments)

def main():
    """Punto de entrada principal del programa"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            print(f"get_jason.py versión {VERSION}")
            sys.exit(0)
        if sys.argv[1] == 'listar':
            log = PaymentsLog.get_instance()
            print("Listado de pagos:")
            for p in log:
                print(f"Pedido {p['pedido']}: {p['monto']} usando {p['token']}")
            sys.exit(0)
        if sys.argv[1] == 'pagar':
            reader = TokenReader.get_instance()
            token1 = reader.get_token('token1')
            token2 = reader.get_token('token2')

            acc1 = AccountHandler("Banco1", 1000, token1)
            acc2 = AccountHandler("Banco2", 2000, token2)
            acc1.set_next(acc2)
            acc2.set_next(acc1)

            for i in range(1, 5):
                acc1.handle_payment(i, 500)
            sys.exit(0)

    print("Uso: python3 get_jason.py [-v | pagar | listar]")
    sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error inesperado: {str(error)}")
        sys.exit(1)

