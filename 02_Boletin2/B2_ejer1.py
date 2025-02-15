# 1 Programa que pida números hasta que se introduzca el 0. Debe calcular la suma 
# y la media de los números introducidos.



num=1
suma = 0
contador = 1

while num != 0:
    num = int(input('Introduce un número: '))
    suma += num
    contador+=1

print(f"la suma es: {suma}")
print(f"la media : {suma/contador}")