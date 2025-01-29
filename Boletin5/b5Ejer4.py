"""
4.- Carga desde teclado la información de los pacientes de un 
determinado hospital perteneciente a una aseguradora privada. 
Sabemos que a través del dni del paciente queremos tener acceso a: 
nombre, edad, si ha sido atendido previamente en ese hospital 
y al código (valor numérico entero) de su médico de cabecera.

- Visualiza la información almacenada.
- Calcula la edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital.
- Visualiza el listado de todos los pacientes de un determinado médico cuyo código se solicitará por teclado.


"""

#vamos a Probar
from random import *

def generaId():
    return random.randint(10000000, 99999999)

def edad():
    return random.randint(15,89)

def aten():
    return random.randint(1,2)



paciente = {
    "idmed": 123,
    "dni": "12345678Z",
    "nombre": "Feliz",
    "edad": 35,
    "aten": 1
}

print("fin")


