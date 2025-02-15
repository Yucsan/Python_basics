# 3 . Escribe un programa que pida por teclado siete números enteros y
#     calcule su suma y su multiplicación.


multi = 1
suma = 0
contador = 0
num = 0

for i in range(7):
    num = int(input('Inserta un número; '))
    suma += num
    multi *= num
print(f"la Suma de los 7 es:{suma} y la Multiplicación de los 7 es {multi}")

