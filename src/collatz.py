#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula el número de pasos de la conjetura de Collatz para n ∈ [1,10000] *
#* y grafica los resultados                                                *
#*-------------------------------------------------------------------------*

import matplotlib.pyplot as plt

#calcular cuántos pasos tarda n en llegar a 1
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

#guardado los valores a graficar
x_vals = []  # n de inicio
y_vals = []  # cantidad de pasos

#n entre 1 y 10000
for n in range(1, 10001):
    x_vals.append(n)
    y_vals.append(collatz_steps(n))

#grafico
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, linewidth=0.7)
plt.title("Conjetura de Collatz: pasos necesarios para n = 1 a 10000")
plt.xlabel("Número inicial n")
plt.ylabel("Cantidad de pasos hasta llegar a 1")
plt.grid(True)
plt.tight_layout()
plt.show()
