
import csv

with open('datos.csv', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    registros = []
    for registro in lector:
        #categoria, dificultad, pregunta, r1,r2,r3,r4, correcta
        print(registro)
        """
        categoria = (registro['categoria'])
        dificultad = (registro['dificultad'])
        pregunta = (registro['pregunta'])
        r1 = (registro['r1'])
        r2 = (registro['r2'])
        r3 = (registro['r3'])
        r4 = (registro['r4'])
        correcta = (registro['correcta'])
        tupla = (categoria, dificultad, pregunta, r1, r2, r3, r4, correcta)
        registros.append(tupla)
        """
    # Mostremos los 10 primeros registros
print(registros[:10])