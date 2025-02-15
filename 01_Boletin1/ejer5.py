# 5.​ Solicitar tres números por teclado y comprobar si alguno de ellos es
# mayor que 10. Mensaje:”Alguno de los 3 números es mayor que 10”


numsEjer5 = []
cuales = [False]*3 #tdos a false
alguno = False


for i in range(3):
    num5 = int(input(f"Inserta numero {i} > "))
    if num5 > 10:
        alguno = True
        cuales[i]=True

if not alguno:
    print(f"No hay mayores de 10")
else:
    print("Alguno es Mayor de 10")
    for i, valor in enumerate(cuales):
        if valor:
            print(f"El: indice: {i} es mayor de 10")  
