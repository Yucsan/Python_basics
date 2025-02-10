

import random

preguntas2 = {
    '1': [
        ('Qué gas da vida a las plantas', ['oxigeno', 'plástico', 'hidrogeno', 'neon'], 'oxigeno', 'fácil'),
         ('¿Cuál es el planeta más cercano al Sol?', ['Mercurio', 'Marte', 'Tierra', 'Venus'], 'Mercurio', 'facil'),
        ('¿Cómo se llama el órgano que bombea la sangre?', ['corazon', 'higado', 'pulmones', 'cerebro'], 'corazon', 'fácil'),

        ('Qué gas da vida a las plantas2', ['oxigeno', 'plástico', 'hidrogeno', 'neon'], 'oxigeno', 'medio'),
         ('¿Cuál es el planeta más cercano al Sol? 2', ['Mercurio', 'Marte', 'Tierra', 'Venus'], 'Mercurio', 'medio'),
        ('¿Cómo se llama el órgano que bombea la sangre 2?', ['corazon', 'higado', 'pulmones', 'cerebro'], 'corazon', 'medio'),

         ('Qué gas da vida a las plantas3', ['oxigeno', 'plástico', 'hidrogeno', 'neon'], 'oxigeno', 'dificil'),
         ('¿Cuál es el planeta más cercano al Sol? 3', ['Mercurio', 'Marte', 'Tierra', 'Venus'], 'Mercurio', 'dificil'),
        ('¿Cómo se llama el órgano que bombea la sangre 3?', ['corazon', 'higado', 'pulmones', 'cerebro'], 'corazon', 'dificil'),


    ],
    '2': [
        ('¿Quién fue el primer presidente de los Estados Unidos?', ['Washington', 'Clinton', 'Trump', 'Obama'], 'Washington', 'fácil'),
        ('¿En qué año cayó el Imperio Romano de Occidente?', ['476', '500', '600', '450'], '476', 'medio'),
        ('¿Qué civilización construyó las pirámides de Egipto?', ['Fenicios', 'Cartagineses', 'Egipcios', 'Griegos'], 'Egipcios', 'facil')
    ],
    '3': [
        ('¿En qué continente se encuentra el desierto del Sahara?', ['Africa', 'Nilo', 'Yangtsé', 'Misisipi'], 'Africa', 'fácil'),
        ('Qué océano rodea la Antártida?', ['Austral', 'Melbourne', 'Canberra', 'Brisbane'], 'Canberra', 'fácil'),
        ('¿Cuál es la montaña más alta del mundo?', ['Everest', 'Mulhacen', 'Pirineaos', 'Huascaran'], 'Everest', 'fácil'),
    ]
}

#1
# print(preguntas2['1'][3][3])


preguntas = {
    '1': [
        ('Qué gas da vida a las plantas', ['oxigeno', 'plástico', 'hidrogeno', 'neon'], 'oxigeno', 'fácil'),
         ('¿Cuál es el planeta más cercano al Sol?', ['Mercurio', 'Marte', 'Tierra', 'Venus'], 'Mercurio', 'facil'),
        ('¿Cómo se llama el órgano que bombea la sangre?', ['corazon', 'higado', 'pulmones', 'cerebro'], 'corazon', 'fácil'),
    ],
    '2': [
        ('¿Quién fue el primer presidente de los Estados Unidos?', ['Washington', 'Clinton', 'Trump', 'Obama'], 'Washington', 'fácil'),
        ('¿En qué año cayó el Imperio Romano de Occidente?', ['476', '500', '600', '450'], '476', 'facil'),
        ('¿Qué civilización construyó las pirámides de Egipto?', ['Fenicios', 'Cartagineses', 'Egipcios', 'Griegos'], 'Egipcios', 'facil')
    ],
    '3': [
        ('¿En qué continente se encuentra el desierto del Sahara?', ['Africa', 'Nilo', 'Yangtsé', 'Misisipi'], 'Africa', 'fácil'),
        ('Qué océano rodea la Antártida?', ['Austral', 'Melbourne', 'Canberra', 'Brisbane'], 'Canberra', 'fácil'),
        ('¿Cuál es la montaña más alta del mundo?', ['Everest', 'Mulhacen', 'Pirineaos', 'Huascaran'], 'Everest', 'fácil'),
    ]
}

dif = ""
textDif = ""
opc = "1"
resp = ""
while opc !="0":
    print("escoge dificultad 1 facil 2 media 3 dificil")
    
    dif = input("inserta opcion")


    print("que categoria quieres? 1 ciencia, 2 historia, 3 geografia ")
    opc = input("inserta opcion")
    if opc == "1" or opc == "2" or opc=="3":

        if dif == '1':
            ale = random.randint(0,2)
        elif dif == '2':
             ale = random.randint(3,5)
        elif dif == '3':
            ale = random.randint(6,8)

        print( preguntas2[opc][ale][0] ) #0-2
        print( preguntas2[opc][ale][1] )

        res = input("ingresa respuesta: ")
        if res == preguntas[opc][ale][2][int(dif)]:
            print("muy bien")
    elif opc == "0":
        print("nos vemos")
        break
    else:
        print("erroneo")


            
"""
falta varias pero estamos en ello
"""             
