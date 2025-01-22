"""


7.​ Escriba un programa que permita crear una lista de palabras 
y que, a continuación de las siguientes opciones:
●​ Contar: Me pide una cadena, y me cuantas veces aparece en la lista
●​ Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
●​ Eliminar: Me pide una cadena, y la elimina de la lista.
●​ Mostrar: Muestra la lista de cadenas
●​ Terminar
"""

lista1 = []

#funciones
def cuenta():
    return len(lista1)

def modifica():

    old = input("inserta palabra a modificar")
    new = input("inserta Nueva palabra")

    print(f"--- modifica ---old: {old} new: {new}")
    for i, text in enumerate(lista1):
        if text == old:
            lista1[i] = new

def elimina():
     cadenaParam = input("inserta Nueva palabra")
     print("--- elimina ---",cadenaParam)
     for i, text in enumerate(lista1):
        if text == cadenaParam:
            del lista1[i]

def muestra():
    print("--- muestro cadena ---")
    for i in lista1:
        print(i)            


#ingresamos cadenas
print("ingresa cadenas de texto para terminar ingresa fin")

cadena = " "
while cadena != "fin":
    cadena = input("ingresa cadena: ")
    lista1.append(cadena)

#menu de copiones
print ("0 cuenta 1 modifica 2 elimina 3 muestra 4 salir" )
print("inserta tu opción: ")
opc = 0
while opc != 4:
    opc = int(input("opcion? "))
    if opc == 0:
        print(f"Nº de cadenas: {cuenta()}")
    elif opc == 1:
        modifica()
    elif opc == 2:
        elimina()
    elif opc == 3:
        muestra()

    print ("0 cuenta 1 modifica 2 elimina 3 muestra 4 salir" )
print("salimos del programa")


