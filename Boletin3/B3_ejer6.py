"""


6.​ Crear un programa que añada números a una lista hasta que
introducimos un número negativo. A continuación debe crear una nueva
lista igual que la anterior pero eliminando los números duplicados.
Muestra esta segunda lista para comprobar que hemos eliminado los
duplicados.
"""

lista1 = []

num = 0
while num >= 0:
    num = int( input("ingresa num: ") )
    lista1.append(num)


lista_sin_duplicados = []
for numero in lista1:
    if numero not in lista_sin_duplicados:
        lista_sin_duplicados.append(numero)

print("Lista original:", lista1)
print("Lista sin duplicados:", lista_sin_duplicados)


    


