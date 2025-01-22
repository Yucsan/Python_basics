#6.​ Nuevo sueldo. Calcular si un empleado aumenta su sueldo. Para ello
# solicitaremos dos valores enteros: sueldo y antigüedad.
# ●​ Si el sueldo es <500 y tiene más de 10 años de antigüedad tendrá el triple de
# su sueldo.
# ●​ Si el sueldo es <500 y tiene menos de 10 años de antigüedad tendrá el doble
# de su sueldo.
# ●​ En cc se queda con el mismo sueldo.


while True:
    try:
        sueldo = int(input("Ingresa tu sueldo: "))
        antiguedad = int(input("Ingresa tu antiguedad: "))
        break
    except ValueError:
        print("solo valores númericos")

if sueldo < 500 and antiguedad > 10:
    print(f"su sueldo es {sueldo*3}€")

elif sueldo < 500 and antiguedad < 10:
    print(f"su sueldo es {sueldo*2}€")
else:
    print(f"su sueldo es {sueldo}€")
