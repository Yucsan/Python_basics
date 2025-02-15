"""


5.​ Diseñar el programa que:
●​ Cree una tabla (lista con dos dimensiones) de 5x5 enteros.
●​ Carga la tabla con valores numéricos enteros.
●​ Suma todos los elementos de cada fila y todos los elementos de
cada columna visualizando los resultados en pantalla.
"""

tabla = [
            [12,15,10,16,8],
            [5,19,14,16,7],
            [12,15,60,16,25],
            [5,10,14,7,30],
            [72,15,10,18,4]
        ]

# suma de filas
for inx ,i in enumerate(tabla):
   print(f" la suma de la fila {inx} es: {sum(i)}" )
print()


#suma de filas
aux=[]
for col in range(5):
    aux=[]
    for i in range(5):
        aux.append(tabla[i][col])
    print(f" la suma en la columna {col} es: {sum(aux)}" )
print()





    


