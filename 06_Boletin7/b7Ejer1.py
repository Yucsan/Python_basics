

"""
Escribe un programa que escriba los 100 primeros números naturales en el archivo numeros.txt.
"""

with open('./salidas/numeros2.txt',mode='w', encoding='utf8') as f:
    for i in range(1,101):
        f.write(str(i)+ '\n')




