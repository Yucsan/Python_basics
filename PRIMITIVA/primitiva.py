

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

jugadores = []
opc = 0

with open('jugadores.csv', encoding='utf8', mode='w', newline='' ) as f:
    escritor = csv.writer(f)
    escritor.writerow(['nombre','apellido']) #escribe encabezado
    escritor.writerow(['Fernando','Chang'])
    escritor.writerow(['Ana','Perez'])


while opc != 6:
    print("opciones: 1. Añadir jugadores \n2. Generar una combinación ganadora \n3. Mostrar los jugadores con sus números \n4. Mostrar los ganadores \n5 Ordenar el fichero por el apellido \n6 Salir")
    opc = int(input('Inserta una opción >:_ '))

    if opc == 6:
        print("fin del Programa")





with open('jugadores.csv', encoding='utf8')as f:
    lector = csv.DictReader(f)

    for i in lector:
        nombre = i['nombre'].strip()
        apellido = i['apellido'].strip()

        tupla = (nombre, apellido)
        jugadores.append(tupla)


for i in jugadores:
    print(i)
