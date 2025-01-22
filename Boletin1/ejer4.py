#4.​ Escribe un programa que pida por teclado siete números enteros
# positivos y calcule su suma y su multiplicación.

numeros = []
multi = 1
suma = 0
contador = 0
num = 0
repetir = 7

while contador < repetir:
    num = int(input('Inserta un número; '))

    if num < 0:
        print(f"el número debe ser mayor que 0 tu número: {num}")
    else:
        numeros.append(num)
        contador+=1  
        

for i in numeros:
    suma += i 
    multi *= i
 
print(f"la Suma de los 7 es:{suma} y la Multiplicación de los {repetir} es {multi}")

