

import controller
import csv
import os
import random



def insertaP():

    palabra = input("inserta palabra ")

    with open( './palabras.csv', encoding='utf8', mode='a+' ) as f:
            escritor = csv.writer(f)
            escritor.writerow([palabra]) 

    print( f"insertada: {palabra}" )

def InsertaNom():
     
    nombre = input("inserta Nombre ")
    
    with open( 'nombres.csv', encoding='utf8', mode='a+' )as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre])
    print("Jugador agregado con exito....")


def guardaGanador(puntos):
    print("** Vamos a guardar tu nombre con tu puntaje **")
    nombre = input("inserta Nombre ")
    
    with open( 'nombres.csv', encoding='utf8', mode='a+' )as f:
        escritor = csv.writer(f)
        escritor.writerow( [ nombre, puntos ] )
    print("Jugador agregado con exito....")    

def maxGanador():

    ganadores = []
    puntajes = []

    with open('nombres.csv', encoding='utf8', mode='r') as f:
        lector = csv.DictReader(f)

        for i in lector:
            nombre = i['nombres']
            puntaje = int(i['puntos'])
       
            ganadores.append(nombre)
            puntajes.append(puntaje)

    maximo = max(puntajes)
    indice = puntajes.index(maximo)
    indices_maximos = [i for i, x in enumerate(puntajes) if x == maximo]

    if len(indices_maximos)>1:
        print("Los jugadores con maximo indice: ")
        for i in indices_maximos:
            print(f" Nombre: {ganadores[i]} puntos: {maximo} ")
    else:        
        print(f"El jugador con máximo puntaje es: {ganadores[indice]} puntaje: {maximo}")        

    
    
def jugar():

    #recoge palabras
    codi = []
    palabras = []
    intentos = 1
    aciertos = 0
    ganas1 = False
    introducidas = []
    restantes = 6
    puntos = 0

    with open('palabras.csv', encoding = 'utf8', mode='r' )as f:
        lector = csv.DictReader(f)
        
        for item in lector:
            palabra = item['palabras'].strip().lower()
            palabras.append(palabra)

    pal = random.choice(palabras)

    for i in pal:
        codi.append("*")

    print("palabra RANDOM", pal) #RECUERDA BORRAR ESTO

    #muestra espacios
    def pinta():
        print("")
        for i in codi:
            print(i, end="")
        print("")

    def muestraIntroducidas():
        print("Letras Ya introducidas: ", end="")

        for i in introducidas:
            print(f" {i} ", end="")
        

    while intentos<=6:
        
        if '*' in codi:
            pinta()
            print("Intentos restantes: ",restantes)
            muestraIntroducidas()
            print("")

            letra = input("inserta Letra ")

            if len(letra)>1:
                 print("debes introducir solo 1 letra")    

            elif letra in pal:
                #print("contiene")

                if letra in introducidas:
                    print("Esa letra ya estaba introducida resta intentos")
                    intentos+=1
                    restantes -= 1
                    controller.muestraImg(restantes)
                else:    
                    aciertos +=1
                    for inx, valor in enumerate(pal):
                        if valor == letra:
                            codi[inx]=letra
                            introducidas.append(letra)

    
            elif letra not in pal:
                intentos +=1
                restantes -= 1
                print("Esa Letra no está en la palabra ")
                introducidas.append(letra)
                controller.muestraImg(restantes)
        else:
            ganas1 = True

            if intentos == 1:
                puntos =150
            elif intentos == 2:
                puntos =100
            elif intentos == 3:
                puntos =75
            elif intentos == 4:
                puntos =50
            elif intentos == 5:
                puntos =25
            elif intentos == 6:
                puntos =10    

            pinta()
            print("********** Ganas *************")
            print(f"Has obtenido: {puntos} puntos")
            maxGanador()
            guardaGanador(puntos)
            break

    if not ganas1:
        print ("****** pierdes ********")
        print("  +----+")
        print("  |    |")
        print("  o    |")
        print("/ | \  |")
        print(" / \   |")
        print("       |")
        print("==========")
        print(" puedes volver a intentar!!!")


def main():

    opc = ""
    print("Juego Ahorcado")
    while opc != "fin":
    
        print("Opciones 1 Introducir palabras 2 Introducir nombre Jugador 3_ Jugar  (fin) salir")
        opc = input("Inserta una Opción: ")

        if opc == "1":
            insertaP()
        elif opc== "2":
            InsertaNom()
        elif opc == "3":
            jugar()
        elif opc =="fin": 
            print("Adios")            
        else:
            print("Opción invalida")

main()            
print("fin del programa")


















