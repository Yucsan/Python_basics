"""

Implementar un programa que permita realizar la operación de copia de un fichero. 
Tanto origen.txt como destino.txt serán ficheros de texto 
cuyos nombres indicará el usuario por teclado.

Se debe utilizar readline() para la lectura del fichero origen y 
comprobar su existencia con os.path.isfile ()
"""


import os


origen = input("Ingresa el nombre del archivo de origen (ej. origen.txt): ")
destino = input("Ingresa el nombre del archivo de destino (ej. destino.txt): ")


if os.path.isfile(origen):
    # Abrir el archivo de origen y el de destino
    with open(origen, mode='r', encoding='utf8') as f_origen, open(destino, mode='w', encoding='utf8') as f_destino:
        # Leer línea por línea del archivo de origen y escribir en el archivo de destino
        line = f_origen.readline()
        while line:
            f_destino.write(line)
            line = f_origen.readline()

    print(f"El archivo '{origen}' se ha copiado correctamente a '{destino}'.")
else:
    print(f"El archivo '{origen}' no existe.")




"""

origen = ""
destino= "copia.txt"
print("****** Ejer 2 *********: ")
origen = input('Ingresa el nombre del fichero de origen: ')
destino = input('Ingresa el nombre del fichero de destino: ')

with open(origen, encoding='utf-8') as f:
   contenido = f.read()

with open(destino,  mode='w', encoding='utf8') as x:
        x.write(contenido) 


"""