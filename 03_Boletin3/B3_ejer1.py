"""
1. Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
""" 

import random

ale =0
l1 = []
cuadrado = 0
cubo = 0

for i in range(0, 10):
    ale = int(random.randint(1, 10))
    l1.append(ale)
    cuadrado = ale*ale
    cubo = ale*ale*ale
    print(f" valor: {ale} cuadrado: {cuadrado} cubo: {cubo}")
