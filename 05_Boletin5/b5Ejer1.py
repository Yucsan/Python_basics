"""
1.- Escribir un programa que procese una serie de cadenas introducidas por teclado. 
Sabemos que la carga de datos finaliza cuando el usuario introduzca la cadena “0”. 
Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.
"""

dic = {}
lista = []

print('para salir presiona 0: ')
opc = 1
while opc != 0:
    opc = int(input('opcion: '))
    if opc == 1:
        cadena = input('inserta cadena: ')
        lista.append(cadena)

for i in lista:
    for j in i:
        if j not in dic:
            dic[j]=1 
        else:
            dic[j]+=1


items = dic.items()
print("valores por caracter: ", items)




print("fin")


