# 2 Escribir un programa que a través de un menú permita al usuario sumar, 
# restar, multiplicar o dividir dos operandos. El menú tendrá la opción 5 de salir.

def sumar(numero1, numero2):   
    resultado = numero1+numero2
    return resultado

def resta(numero1, numero2):    
    resultado = numero1-numero2
    return resultado

def multi(numero1, numero2):    
    resultado = numero1*numero2
    return resultado

def divi(numero1, numero2): 
    if(numero2 != 0 ):   
        resultado = numero1/numero2
        return resultado
    else: print("no se puede divir entre cero")

        
opcion = 1 # para que entre
while opcion != 5:
    print("1 suma, 2 restar, 3 multiplicar, 4 Dividir, 5 salir")
    opcion = int(input('Introduce un opcion: '))

    if opcion == 1:
        num1 = int(input('Introduce un número: '))
        num2 = int(input('Introduce un número: '))
        print( f"suma: {sumar(num1,num2)}" )
    elif opcion == 2:
        num1 = int(input('Introduce un número: '))
        num2 = int(input('Introduce un número: '))
        print( f" resta: {resta(num1,num2)}" )
    elif opcion == 3:
        num1 = int(input('Introduce un número: '))
        num2 = int(input('Introduce un número: '))
        print( f" multi {(num1,num2)}" )
    elif opcion == 4:            
        num1 = int(input('Introduce un número: '))
        num2 = int(input('Introduce un número: '))
        print( f" division: {divi(num1,num2)}" )


print("salimos")    
