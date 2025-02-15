"""
2.- Modifica el ejercicio anterior para que el programa 
informe del número de ocurrencias de las distintas letras 
del alfabeto incluyendo aquellas que no aparezcan (indicar valor 0)

"""

dic = {}
lista = []

#creamos alfabeto
letras ="abcdefghijklmnñopqrstuvwyz"

for i in letras:
    dic[i]=0


print('para salir presiona 0: ')
opc = 1
while opc != 0:
    opc = int(input('opcion: '))
    if opc == 1:
        cadena = input('inserta cadena: ').lower()
        lista.append(cadena)

for i in lista:
    for j in i:
        if j in dic:
            dic[j]+=1 


print(dic)

print("fin")


