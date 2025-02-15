# Solicitar una nota (float) y mostrar mensaje:
# Si nota < 3: “muy deficiente”
# Si nota < 5: “insuficiente”
# Si nota < 6: “suficiente”
# Si nota < 7:”bien”
# Si nota < 9: “notable”
# Si nota <10: “sobresaliente”

while True:
    try:
        nota = float(input("Ingresa tu nota: "))
        break
    except ValueError:
        print("solo valores númericos")

if nota < 3.0:
    print("muy deficiente")        
elif nota < 5.0:
    print("insuficiente")        
elif nota <= 6.0:
    print("Suficiente")  
elif nota <= 7.0:
    print("bien")
elif nota <= 9.0:
    print("Notable")
elif nota >= 10.0:
    print("Sobresaliente")    