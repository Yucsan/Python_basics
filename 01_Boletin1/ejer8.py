#numeros primos opcion1

esPrimo = True

numeroP = int(input("inserta un número: "))
if numeroP <=1:
    esPrimo = False

for i in range(2, int(numeroP**0.5) +1 ):
    if numeroP % i == 0:
         esPrimo = False

if esPrimo:
    print(f"{numeroP} Es primo")
else:
    print(f"{numeroP} NO es primo")


#numeros primos opcion 2   -------------------------------------------------------------------- 

from math import sqrt #otra forma de usar raiz cuadrada importando math

esPrimo2 = True

numeroP2 = int(input("inserta un número: "))
if numeroP2 <=1:
    esPrimo2 = False

for i in range(2, int(sqrt(numeroP2)) +1 ):
    if numeroP2 % i == 0:
         esPrimo2 = False

if esPrimo2:
    print(f"{numeroP2} Es primo")
else:
    print(f"{numeroP2} NO es primo")


"""
Cuando el exponente es una fracción como 1/21/2, 1/31/3, 1/41/4, etc.:

Por ejemplo:

    A elevado 1/2 = A raiz cuadrada de A
    A elevado 1/3 = A raiz cúbica de A
    A elevado 1/4 = A raiz cuarta de A
"""