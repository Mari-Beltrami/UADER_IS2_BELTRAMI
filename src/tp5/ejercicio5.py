#*--------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento
#* Memento con múltiples estados
#*--------------------------------------------------------------------

import os

#* Clase Memento para guardar el estado del archivo
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


#* Clase que representa el recurso cuyo estado queremos guardar/restaurar
class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


#* Clase que gestiona la lista de mementos
class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        if len(self.history) == 4:
            self.history.pop(0)  # elimina el más antiguo
        self.history.append(writer.save())

    def undo(self, writer, index=0):
        if 0 <= index < len(self.history):
            writer.undo(self.history[-(index+1)])
        else:
            print(f"Índice {index} inválido. No se pudo deshacer.")


#* Bloque principal de ejecución
if __name__ == "__main__":
    os.system("clear")
    print("\n--- Memento con múltiples versiones (hasta 4) ---\n")

    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("IS2_UADER.txt")

    print("Estado 1:")
    writer.write("Versión 1: Introducción a patrones\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nEstado 2:")
    writer.write("Versión 2: Agregamos Factory Method\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nEstado 3:")
    writer.write("Versión 3: Incorporamos Decorator\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nEstado 4:")
    writer.write("Versión 4: Aplicamos Observer\n")
    print(writer.content)
    caretaker.save(writer)

    print("\nEstado 5 (no guardado):")
    writer.write("Versión 5: Agregamos Strategy\n")
    print(writer.content)

    print("\n→ Undo(0): Recupera última versión guardada")
    caretaker.undo(writer, 0)
    print(writer.content)

    print("\n→ Undo(2): Recupera versión 2")
    caretaker.undo(writer, 2)
    print(writer.content)

    print("\n→ Undo(4): Intento inválido")
    caretaker.undo(writer, 4)
