"""
2. Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
"""

notas = []

for i in range(5):
    aux = int(input('Ingresa 1 nota: '))
    if aux < 0 or aux > 10:
        print("Las notas deben estar entre 1 y 10")
    else:
        notas.append(aux)

notas.sort()
media = (sum(notas)) / len(notas)

print("notas:", end=" ")
for i in notas:
    print(i, end=", ")

print( f"La notas mas alta: {notas[-1]} , lá mas baja : {notas[0]} y la media: {media} " )
