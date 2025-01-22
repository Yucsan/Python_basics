# 5 Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("ingresa una frase: ")
letraBusca = input("ingresa una letra: ")
cuenta = 0

for letra in frase:
    if letra == letraBusca:
        cuenta +=1

if(cuenta == 0):
    print(f"No hay letra {letraBusca}")
else:
    print(f"en la frase hay {cuenta} coincidencias")    