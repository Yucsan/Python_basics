"""
Escribir una función, obtenerNumerosArchivo, 
que reciba por parámetro el nombre de un archivo 
que almacenará una serie de cantidades 
enteras y positivas (un número por línea). 
La función leerá todos los valores del archivo, 
calculará su suma y la devolverá.

"""

def obtenerNumerosArchivo(nombreFichero):
    suma = 0
    with open(nombreFichero, mode='r', encoding='utf8') as f:
        for line in f:  # Lee cada línea del archivo
            aux = line.strip()  # Elimina los saltos de línea y los espacios en blanco
            suma += int(aux) 

    print(suma)

obtenerNumerosArchivo('./salidas/numeros2.txt')