

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
import random
import time
# categoria,dificultad,pregunta,r1,r2,r3,r4,correcta

registros = []

filtrado = [] # filtro preguntas de la categoria que se elije

puntaje = 0
reglasPuntos = (1,5,7)

preguntas = {
    'ciencia':[],
    'historia':[],
    'geografia':[],
}

with open('datos.csv', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for registro in lector:
        
        categoria = registro['categoria'].strip()
        pregunta = registro['pregunta'].strip()
        r1 = registro['r1'].strip()
        r2 = registro['r2'].strip()
        r3 = registro['r3'].strip()
        r4 = registro['r4'].strip()
        correcta = registro['correcta'].strip()

        nivel = registro['dificultad'].strip()

        tupla2 = (categoria, pregunta, r1,r2,r3,r4, correcta, nivel)
        registros.append(tupla2)

        if categoria == 'ciencia':
            preguntas['ciencia'].append(tupla2)
        elif categoria == 'historia':
            preguntas['historia'].append(tupla2)
        else:
            preguntas['geografia'].append(tupla2)   

dif = 0
textDif = ""
opc = 1
resp = ""
nivel = ""
categoriaElegida = ''

print(" ****** JUEGO TRIVIA PABLO / FERNANDO  ******* ")
while opc != 100:


    print("Escoge dificultad: (1)facil (2)media  (3)dificil.")
    print(f"*** PUNTAJE ACUMULADO: {puntaje} puntos")
    dif = int(input("inserta opcion (100 para salir):..> "))

    if dif == 100:
        print("Nos vemos.")
        break

    print("que categoria quieres? 1 ciencia, 2 historia, 3 geografia.")
    opc = int(input("inserta opcion (0 para salir): "))

    if dif == 1:
        nivel = "facil"
    elif dif == 2:
        nivel = "media"
    else:
        nivel = "dificil"  

    ale = 0
    if opc == 1 or opc == 2 or opc==3:

        if dif == 1:
            categoriaElegida = 'ciencia'
        elif dif == 2:
            categoriaElegida = 'historia'
        elif dif == 3:
            categoriaElegida = 'geografia'

        print("------")
                                                #filtro todas las preguntas de la categoria y nivel seleccionada
        for i in preguntas[categoriaElegida]:     
            if i[7] == nivel:
                filtrado.append(i)
        #print(filtrado)  

        ale = random.randint(0, len(preguntas[categoriaElegida])-1 ) #Genero Nº aleatorio segun el Nº d preguntas
        
        print( "pregunta: ", preguntas[categoriaElegida][ale][1] ) #muestro la pregunta elegida
        print( "opciones: ", end=" ")

                            #muestro las opciones de la respuesta 2,3,4,5 de la pregunta elegida ale
        for i in range(2,6):
            print(preguntas[categoriaElegida][ale][i], end=" ")  

        tiempo = time.time() #declaramos tiempo
        res = int(input("ingresa respuesta: ").lower().strip())
        
        aux = 0
        resElegida = ""

        if res == 1:
            aux = 2
        elif res == 2:
           aux = 3
        elif res == 3:
           aux = 4
        elif res == 4:
            aux = 5

        resElegida = preguntas[categoriaElegida][ale][aux]
    
        print("tu respuesta", resElegida)
        #print("comprueba respuesta correcta", preguntas[categoriaElegida][ale][6].lower().strip())

        tiempoRespuesta = time.time() - tiempo
        #comprobamos respuesta
        if resElegida.lower() == preguntas[categoriaElegida][ale][6].lower().strip() and tiempoRespuesta <= 6 : 
          
            print("¡Muy bien!")
            print(f"has respondido en {tiempoRespuesta} segundos")
            if nivel == "facil":
                puntaje= puntaje+reglasPuntos[0]
            elif nivel == "media":
                puntaje= puntaje+reglasPuntos[1]
            elif nivel == "dificil":
                puntaje= puntaje+reglasPuntos[2]

        elif tiempoRespuesta > 6:
            print(f"has respondido en {tiempoRespuesta} segundos")
            print("te pasaste de tiempo tienes solo 6 segundos para responder")

        else:
            print(f"has respondido en {tiempoRespuesta} segundos")
            print("¡Mal!")


    elif opc == "100":
        print("Nos vemos.")
        break
    else:
        print("Opción errónea.")
    
    print(" ")
    


print("sales del programa")