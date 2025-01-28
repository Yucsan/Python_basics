
lista = {}
opc = 1

"""
Añadir un nuevo par clave-valor.
Listar todas las claves y sus valores
Eliminar una clave y su valor asociado.
Buscar el valor de una clave específica.
Listar todas las claves del diccionario.
Listar todos los valores del diccionario.
Listar todos los pares clave-valor del diccionario.

Comprobar si una clave existe en el diccionario.
Calcular la suma de todos los valores del diccionario (asumiendo que los valores son numéricos).

Obtener la clave máxima y mínima del diccionario.
Obtener el número total de elementos en el diccionario.

"""
print(" opciones 1,2,3,4,5,6,7,8, 0 para salir")
while opc != 0:
    opc = int(input('ingresa opcion '))
    if opc == 1:
         clave = input("inserta nombre: ")
         valor = input("inserta nombre: ")
         lista[clave]=valor
    
    elif opc == 2:
        print(lista)

    elif opc == 3:
        clave = input("inserta nombre: ")
        del lista[clave]
    elif opc == 4:
        clave = input("inserta nombre a buscar: ")
        print("su valor es: ", lista.get(clave) )

    elif opc == 5:

        claves = lista.keys()
        print("Claves del diccionario:", claves)

    elif opc == 6:
        valores = lista.values()
        print("Claves del diccionario:", valores)
    elif opc == 7:    
        items = lista.items()
        print("Pares clave-valor del diccionario:", items)

    elif opc == 8:
        clave = input("inserta nombre a buscar: ")    
        print(f"{clave} esta: ?", clave in lista)

    elif opc == 9:
        suma_cantidades = sum(lista.values())
        print("Suma de cantidades de productos:", suma_cantidades)

    elif opc == 10:
        max_clave = max(lista)
        print("Máxima clave del diccionario:", max_clave)

    elif opc == 11:
        longitud_diccionario = len(lista)
        print("Número de elementos en el diccionario:", longitud_diccionario)
 


        

print("salimos")   