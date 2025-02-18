

""" 
El programa debe permitir:
1. Añadir jugadores
2. Generar una combinación ganadora
3. Mostrar los jugadores con sus números
4. Mostrar los ganadores
5. Ordenar el fichero por el apellido
6. Salir
El programa debe solicitar por teclado el nombre y apellido ,
generar aleatoriamente siete números para cada jugador y
almacenarlos en un fichero .csv.
La estructura será:

nombre,apellido1,num1,num2,num3,num4,num5,num6,num7
Se debe generar la combinación ganadora antes de ver los
ganadores.
El programa debe generar una combinación ganadora de 6
números, mostrar los nombres de los jugadores y sus
números , e indicar si algún jugador ha ganado un premio.
Los premios se otorgan según la cantidad de números
acertados.
Premios:

2 números acertados: 1.000 euros
3 números acertados: 8.000 euros.
4 números acertados: 20.000 euros.
5 números acertados: 150.000 euros.
6 números acertados: 1.000.000 euros.

"""
import csv
import os
import random

jugadores = [] #lista local
opc = 0
comboGanador = []

import controlador

# si existe abrimos fichero con nombre de jugadores //

controlador.cargarData(jugadores)

# ------------------  bucle principal  
while opc != 6:
    print("opciones: \n 1. Añadir jugadores")
    print("2. Generar una combinación ganadora")
    print("3. Mostrar los jugadores con sus números")
    print("4. Mostrar los ganadores")
    print("5 Ordenar el fichero por el apellido")
    print("6 salir")
    
    opc = int(input('Inserta una opción >:_ '))

    if opc == 1:
        controlador.agregaJugador(jugadores)
    
    elif opc == 2:
        controlador.numGanador(jugadores, comboGanador)

    elif opc == 3:
        controlador.mostrarJugadores(jugadores)

    elif opc == 4:
        controlador.ganadores(comboGanador, jugadores)

    elif opc == 5:
        controlador.ordena()    
      
    elif opc == 6:
        print("NOS VEMOS")

print("fin del Programa")




