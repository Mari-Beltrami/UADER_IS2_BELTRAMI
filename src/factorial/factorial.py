#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o rango                               *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#si se omite el número como argumento, solicitarlo
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej. 5, 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

#saber si es núm único o rango
if '-' in entrada:
    partes = entrada.split('-')
    
    #"-hasta"
    if partes[0] == '' and partes[1].isdigit():
        hasta = int(partes[1])
        desde = 1
        print(f"Calculando factoriales entre {desde} y {hasta}")
        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")

    #"desde-"
    elif partes[1] == '' and partes[0].isdigit():
        desde = int(partes[0])
        hasta = 60
        print(f"Calculando factoriales entre {desde} y {hasta}")
        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")

    #"desde-hasta"
    elif partes[0].isdigit() and partes[1].isdigit():
        desde = int(partes[0])
        hasta = int(partes[1])
        print(f"Calculando factoriales entre {desde} y {hasta}")
        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")

    else:
        print("Formato de rango inválido.")
else:
    num = int(entrada)
    print(f"{num}! = {factorial(num)}")


