

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

def mostrarJugadores():
    for i in jugadores:
        print(f"{i}")


# si existe abrimos fichero con nombre de jugadores
if os.path.isfile("./jugadores.csv"):
    print("ya existe el archivo")
else:
    print("NO existe el archivo lo creammos")    
    with open('jugadores.csv', encoding='utf8', mode='w', newline='' ) as f:
        escritor = csv.writer(f)
        escritor.writerow(['nombre','apellido']) #escribe encabezado
        escritor.writerow(['Fernando','Chang'])
        escritor.writerow(['Ana','Perez'])

with open('jugadores.csv', encoding='utf8')as f:
    lector = csv.DictReader(f)
    
    for i in lector:
        nombre = i['nombre'].strip()
        apellido = i['apellido'].strip()
        Lista = [nombre, apellido,0,0,0,0,0,0,0,0]
        jugadores.append(Lista)

#------------------------------------muestra
def mostrarJugadores():
    print("Muestro Jugadores y sus Números")
    for i in jugadores:
        print(i)

#--------------------------------------------------------------- GENERO Numeros Ganadores
def numGanador():
    global comboGanador
    comboGanador = [] #limpio Nºs ganadores

    for jug in jugadores: #limpio anteriores coincidencias
        jug[9] = 0

    for i in range(7):
        ale = random.randint(1,49)
        comboGanador.append(ale)

    print(comboGanador)

    generaNumeros()    

#agrega aleatorios a los jugadores
def generaNumeros():
  print("entro")
  for i in jugadores:
    for j in range(2,9):
        ale = random.randint(1,49)    
        i[j]=ale

#---------------------------------------- comprueba Ganador
def ganadores():
    print("numeros ganadores")
    print(comboGanador)
    aux = []
    for persona in jugadores:
        aux = persona[2:8]
        for num in aux:
           
           if num in comboGanador:  # si numero esta Los Nº ganadores
               persona[9]= persona[9]+1
  
    # si hay coincidencias muestro premios
    ganadores = []
    for persona in jugadores:
        
        gana = 0
        if persona[9] >=2:
            if persona[9] == 2:
                gana = 1000
            elif persona[9] == 3:
                gana = 8000
            elif persona[9] == 4:
                gana = 20000
            elif persona[9] == 5:
                gana = 150000
            elif persona[9] == 6:
                gana = 1000000

            ganadores.append( (persona[0], persona[1], gana) )

    if ganadores:
        for ganador in ganadores:
            print(f"{ganador[0]} {ganador[1]} gana: {ganador[2]}€")
    else:
        print("no hay ganadores")          

#-------------------- ordena y reescribe el fichero ordenado por apellido
def ordena():
    jugadoresOrdenados = []
    with open('jugadores.csv', encoding='utf8')as f:
        lector = csv.DictReader(f)  

        for i in lector:
            nombre = i['nombre'].strip()
            apellido = i['apellido'].strip()
            Lista = [nombre, apellido]
            jugadoresOrdenados.append(Lista)

    jugadoresOrdenados.sort(key=lambda x: x[1])

    with open('jugadores.csv', mode='w', encoding='utf8', newline='') as f:
        escritor = csv.writer(f)

        escritor.writerow(['nombre', 'apellido'])
        for jug in jugadoresOrdenados:
            escritor.writerow(jug)

    print(jugadoresOrdenados)


# ------------------  bucle principal  
while opc != 6:
    print("opciones: \n 1. Añadir jugadores \n2. Generar una combinación ganadora \n3. Mostrar los jugadores con sus números \n4. Mostrar los ganadores \n5 Ordenar el fichero por el apellido \n6 Salir")
    opc = int(input('Inserta una opción >:_ '))

    if opc == 1:
        nombre = input('Inserta Nombre: ')
        apellido = input('Inserta Apellido: ')
        nuevoJugador = [nombre, apellido,0,0,0,0,0,0,0]
        jugadores.append(nuevoJugador)

        with open('jugadores.csv', mode='a', encoding='utf8') as f:
            escritor = csv.writer(f)
            escritor.writerow([nombre, apellido])

    elif opc == 2:
        numGanador()

    elif opc == 3:
        mostrarJugadores()    

    elif opc == 4:
        ganadores()

    elif opc == 5:
        ordena()    
      
    elif opc == 6:
        print("NOS VEMOS")

    elif opc == 7:
            print(comboGanador)

print("fin del Programa")




