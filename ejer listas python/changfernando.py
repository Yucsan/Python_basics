
lista = []
copia = []
pesos = []

opc = 1

def insertaNombre():
    for i in range(5):
        aux = input("inserta nombre: ")
        lista.append(aux)
    print("fin1")

def muestraLista1():
    #muestra el listado
    for i in lista:
        print(i)
    print("fin muestralista1")


#borrado
def borra():
    borra = input("inserta nombre a borrar: ")
    for i,val in enumerate(lista):
        if val == borra:
            del lista[i]
    print("se ha borrado")        



#agrega a la segunda y muestras las 2 listas
def agrega2():
    agrega2 = input("inserta nombre a agregar a la lista2: ")
    copia.append(agrega2)

    for i in lista:
        print(i)

    for j in copia:
        print(j)

    print("fin agrega2")    


#3era lista

def creaLista3():
    pesitos = [53.2,141.8,105.3,78.2,60.4]
    for i in pesitos:
        pesos.append(i)

def muestralista3():
    print("muestra los contenidos")
    for i in pesos:
        print(i)

    media = (sum(pesos))/len(pesos)
    print("la media es: ",media)

    pesos.sort()
    maxima = pesos[-1]
    print("max:", maxima)
    minima = pesos[0]
    print("min",minima)

    print("fin muestralista3")


def muestraMax():
    cuenta = 0
    for i,val in enumerate(pesos):
        if val > 100:
            print("la persona con mas de 100 es: ", i)
            cuenta+=1
    print(f"hay ${cuenta} con mas de 100 kg")



print(" opciones 1,2,3,4,5,6,7,8, 0 para salir")
while opc != 0:
    opc = int(input('ingresa opcion '))
    if opc == 1:
        insertaNombre()
    elif opc == 2:
        muestraLista1()
    elif opc == 3:
        borra()
    elif opc == 4:
        copia = list(lista)
    elif opc == 5:
        agrega2()
    elif opc == 6:
        creaLista3()
    elif opc == 7:    
        muestralista3()
    elif opc == 8:    
        muestraMax()   

print("salimos")   













