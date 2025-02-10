

import random


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


opc = "1"
resp = ""
while opc !="0":
    print("que categoria quieres? 1 ciencia, 2 historia, 3 geografia ")
    opc = input("inserta opcion")
    if opc == "1" or opc == "2" or opc=="3":
        ale = random.randint(0,2)
        print(preguntas[opc][ale][0])
        print(preguntas[opc][ale][1])
        res = input("ingresa respuesta: ")
        if res == preguntas[opc][ale][2]:
            print("muy bien")
    elif opc> "3":
        print("opcion erronea")
            
"""
falta varias pero estamos en ello
"""             
