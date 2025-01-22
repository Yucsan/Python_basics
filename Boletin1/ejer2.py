# 2. Idem al anterior pero definiendo una función

def raiz():
    print(" ingresa una base ")
    base = input ("base: -> ")
    print(" ingresa un exponente ")
    expo = input ("exponente: -> ")
    print (f"la base {base} elevado a {expo} = {float(base)**float(expo)}")

raiz()