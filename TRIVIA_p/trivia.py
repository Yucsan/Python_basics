import random
# categoria,dificultad,pregunta,r1,r2,r3,r4,correcta



# solo funcionan las preguntas de la categoria 1




"""
preguntas = {
    '1': [
        #Fáciles
        ('Qué gas da vida a las plantas', ['Oxígeno', 'Plástico', 'Hidrogeno', 'Neon'], 'Oxígeno'),
        ('¿Cuál es el planeta más cercano al Sol?', ['Mercurio', 'Marte', 'Tierra', 'Venus'], 'Mercurio'),
        ('¿Cómo se llama el órgano que bombea la sangre?', ['Corazón', 'Higado', 'Pulmones', 'Cerebro'], 'Corazón'),
        #Medias
        ('¿Cómo se llama el proceso por el cual las plantas producen su propio alimento?', ['Protón', 'Electrón', 'Neón', 'Xenón'], 'Electrón'),
        ('¿Cuál es el planeta más grande del sistema solar?', ['Júpiter', 'Urano', 'Mercurio', 'Tierra'], 'Júpiter'),
        ('¿Cómo se llama el proceso por el cual las plantas producen su propio alimento?', ['Necrosis', 'Fagocitosis', 'Fotosíntesis', 'Respiración'], 'Fotosíntesis'),
        #Difíciles
        ('¿Qué fenómeno físico describe la resistencia de un fluido al movimiento de un objeto a través de él?', ['Hidrógeno', 'Mercurio', 'Oganesón', 'Oxígeno'], 'Oganesón'),
        ('¿Cómo se llama la partícula hipotética que mediaría la fuerza gravitatoria en la teoría cuántica?', ['Quark', 'Neutrino', 'Fotón', 'Gravitón'], 'Gravitón'),
        ('¿Qué fenómeno físico describe la resistencia de un fluido al movimiento de un objeto a través de él?', ['Viscosidad', 'Inercia', 'Entropía', 'Presión'], 'Viscosidad'),
    ],
    '2': [
        #Fáciles
        ('¿Quién fue el primer presidente de los Estados Unidos?', ['Washington', 'Clinton', 'Trump', 'Obama'], 'Washington'),
        ('¿En qué año cayó el Imperio Romano de Occidente?', ['476', '500', '600', '450'], '476', 'medio'),
        ('¿Qué civilización construyó las pirámides de Egipto?', ['Fenicios', 'Cartagineses', 'Egipcios', 'Griegos'], 'Egipcios'),
        #Medias
        ('¿En qué año comenzó la Revolución Francesa?', ['1492', '1917', '1789', '1815'], '1789'),
        ('¿Qué civilización construyó Machu Picchu?', ['Mayas', 'Incas', 'Aztecas', 'Egipcios'], 'Incas'),
        ('¿Quién fue el primer emperador de Roma?', ['Nerón', 'Augusto', 'Julio', 'Trajano'], 'Augusto'),
        #Difíciles
        ('¿Qué tratado puso fin a la Primera Guerra Mundial?', ['Versalles', 'Tordesillas', 'Utrecht', 'Yalta'], 'Versalles'),
        ('¿Qué civilización antigua desarrolló la escritura cuneiforme?', ['Egipcia', 'Fenicia', 'Persa', 'Sumeria'], 'Sumeria'),
        ('¿En qué isla fue desterrado Napoleón tras su derrota definitiva?', ['Elba', 'Sicilia', 'Santa Elena', 'Malta'], 'Santa Elena')
    ],
    '3': [
        #Fáciles
        ('¿En qué continente se encuentra el desierto del Sahara?', ['África', 'Asia', 'América', 'Oceanía'], 'Africa'),
        ('Qué océano rodea la Antártida?', ['Austral', 'Melbourne', 'Canberra', 'Brisbane'], 'Austral'),
        ('¿Cuál es la montaña más alta del mundo?', ['Everest', 'Mulhacen', 'Pirineos', 'Huascaran'], 'Everest'),
        #Medias
        ('¿Cuál es el país más grande del mundo en superficie?', ['Canadá', 'China', 'Rusia', 'Estados Unidos'], 'Rusia'),
        ('¿Qué océano es el más profundo del planeta?', ['Atlántico', 'Índico', 'Pacífico', 'Ártico'], 'Pacífico'),
        ('¿Qué país tiene la mayor cantidad de islas en el mundo?', ['Suecia', 'Canadá', 'Noruega', 'Indonesia'], 'Suecia'),
        #Difíciles
        ('¿Cuál es el río más largo del mundo?', ['Amazonas', 'Nilo', 'Yangtsé', 'Misisipi'], 'Nilo'),
        ('¿Qué montaña es la más alta de África?', ['Kilimanjaro', 'Everest', 'Atlas', 'Kenia'], 'Kilimanjaro'),
        ('¿Qué país tiene la mayor extensión territorial en América del Sur?', ['Argentina', 'Chile', 'Colombia', 'Brasil'], 'Brasil')
    ]
}
"""

import csv

registros = []
with open('datos.csv', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for registro in lector:
        #categoria, pregunta, r1,r2,r3,r4, correcta
        categoria = (registro['categoria'])
        pregunta = (registro['pregunta'])
        r1 = (registro['r1'])
        r2 = (registro['r2'])
        r3 = (registro['r3'])
        r4 = (registro['r4'])
        correcta = (registro['correcta']).strip()
        tupla = (categoria, pregunta, r1, r2, r3, r4, correcta)
        registros.append(tupla)

dif = 0
textDif = ""
opc = 1
resp = ""

while opc != 100:

    print("escoge dificultad: 1 facil 2 media 3 dificil.")
    dif = int(input("inserta opcion (0 para salir): "))

    if dif== 100:
        print("Nos vemos.")
        break

    print("que categoria quieres? 1 ciencia, 2 historia, 3 geografia.")
    opc = int(input("inserta opcion (0 para salir): "))

    if opc == 1 or opc == 2 or opc==3:

        if dif == 1:
            ale = random.randint(0,2)
            print("q sale: ",ale)
        elif dif == 2:
             ale = random.randint(3,5)
        elif dif == 3:
            ale = random.randint(6,8)

        print( registros[ale][opc] )
        print( registros[ale][2], registros[ale][3], registros[ale][4], registros[ale][5] )

        res = input("ingresa respuesta: ").strip()

        print(res)
        print(registros[ale][6])

        if res.strip() == registros[ale][6]:
          
            print("¡Muy bien!")
        else:
            print("¡Mal!")
    elif opc == "100":
        print("Nos vemos.")
        break
    else:
        print("Opción errónea.")