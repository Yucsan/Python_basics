
import csv
import os

# 0 ======   CARGAMOS EL ARCHIVO
def cargarData(jugadores):
    print("me llaman")
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

#  1 ------------------------------- 1 AGREGA JUGADORES
def agregaJugador(jugadores):
    nombre = input('Inserta Nombre: ')
    apellido = input('Inserta Apellido: ')
    nuevoJugador = [nombre, apellido,0,0,0,0,0,0,0,0]
    jugadores.append(nuevoJugador)

    with open('jugadores.csv', mode='a', encoding='utf8') as f:
            escritor = csv.writer(f)
            escritor.writerow([nombre, apellido])

# 2  --------------------------------------- GENERO Numeros Ganadores
def numGanador():
    global comboGanador
    comboGanador = [] #limpio Nºs ganadores

    for jug in jugadores: #limpio anteriores coincidencias
        jug[9] = 0

    for i in range(7):  #Genero Nums aleatorios 
        ale = random.randint(1,49)
        comboGanador.append(ale)

    print(f" Este Son Los Nums Ganadores {comboGanador}")
    generaNumeros()    

#agrega aleatorios a los jugadores
def generaNumeros():
  print("entro")
  for i in jugadores:
    for j in range(2,9):
        ale = random.randint(1,49)    
        i[j]=ale

# 3 mostrar jugadores
def mostrarJugadores(jugadores):
    print("***********  MUESTRO JUGADORES CON SUS NUMEROS ***********")
    print("Muestro Jugadores y sus Números")
    for i in jugadores:
        print(i)

# 4 --------------------------------------- comprueba Ganador
def ganadores(comboGanador):
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
        print( " **********  Numeros  Ganadores ********** ")
        for ganador in ganadores:
            print(f"{ganador[0]} {ganador[1]} gana: {ganador[2]}€")
    else:
        print(" *********  NO Hay Ganadores  *********") 

    #- 5 ------------------ ordena y reescribe el fichero ordenado por apellido
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