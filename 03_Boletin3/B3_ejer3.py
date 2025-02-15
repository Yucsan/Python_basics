
"""
3. Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
y posterior ordene los elementos de menor a mayor.
"""

import random

numerosAle = []

for i in range(10):
    ale = int(random.randint(0, 80))
    numerosAle.append(ale)

numerosAle.sort()
numerosAle.reverse()
print("los valores ordenados son: ",end="")
for i in numerosAle:
    print(i, end=" ")

