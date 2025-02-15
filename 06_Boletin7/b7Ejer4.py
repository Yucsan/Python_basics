"""
Escriba un programa que se encargue de clasificar 
una serie de cadenas atendiendo a su longitud. 
Se solicitará al usuario el nombre del archivo 
que contendrá el conjunto de palabras, cada una en una línea. 
También se pedirá por teclado un valor entero 
que se utilizará como valor de corte para clasificar 
las palabras del archivo anterior. 
Las palabras con longitud menor al valor de 
corte se almacenarán en el fichero menor.txt y 
el resto de palabras en el fichero mayor.txt

"""

nombres = []
origen = input('ingresa archivo de origen: ')
numero = int( input('valor númerico: ') )

with open(origen, mode='r', encoding='utf8' ) as f:
    for line in f:
        nombres.append(line)

for i in range(numero):
    with open('./salidas/min.txt', mode='a', encoding='utf8' )as f:
        f.write(nombres[i])

for i in range(numero, len(nombres) ):
    with open('./salidas/man.txt', mode='a', encoding='utf8' )as f:
        f.write(nombres[i])
