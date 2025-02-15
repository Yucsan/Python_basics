"""
4.- Carga desde teclado la información de los pacientes de un 
determinado hospital perteneciente a una aseguradora privada. 
Sabemos que a través del dni del paciente queremos tener acceso a: 
nombre, edad, si ha sido atendido previamente en ese hospital 
y al código (valor numérico entero) de su médico de cabecera.

- Visualiza la información almacenada.
- Calcula la edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital.
- Visualiza el listado de todos los pacientes de un determinado médico cuyo código se solicitará por teclado.

esto es mi modelo
paciente = {
    "idmed": 123,
    "dni": "12345678Z",
    "nombre": "Feliz",
    "edad": 35,
    "aten": 1
}

test

"""

# FUNCIONES para llenado random
import random

def generaId():
    return random.randint(10000000, 99999999)

def edad():
    return random.randint(15,89)

def aten():
    aux = random.randint(1,2)
    return aux == 1 

def nombre():
    aux = random.randint(0,len(nombres)-1)
    return nombres[aux]

#Calcula la edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital.
def edadM():
    for p in pacientes:
        if p['aten']:
            auxEdades.append(p['edad'])

    aux = sum(auxEdades)/len(auxEdades)
    if aux:
        print("edad media de atendidos: ",aux)

#muestra pacientes de 1 medico por id
def listaId():
    idin = int(input("ingresa id numerico: "))

    encontrados = False

    for paciente in pacientes:
        if paciente['idmed'] == int(idin):
            print(paciente)

    if not encontrados:
        print("Sin pacientes ese id")

def agregaPaciente():            
    idmedIn = int(input("inserta idmed: "))
    dniIn = input("inserta dni: ")
    nombreIn = input("inserta nombre: ")
    edadIn = input("inserta edad: ")
    atenIn = input("inserta aten: ")

    paciente={
        "idmed": idmedIn,
        "dni": dniIn,
        "nombre": nombreIn,
        "edad": edadIn,
        "aten": atenIn 
    }
    pacientes.append(paciente)


#DATA se simula una data ya existente
auxEdades=[]
nombres = ["María","Jose","Pedro","Korra","Jenny","Chiara"]
pacientes = []

for i in range(3):
    paciente={"idmed": i,
    "dni": generaId(),
    "nombre": nombre(),
    "edad": edad(),
    "aten": aten()
    }
    pacientes.append(paciente)

edadM()


#MENU
opc = 1
while opc !='0':
    print("1 -> Ver Pacientes ")
    print("2 -> edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital  ")
    print("3 -> Lista pacientes por id de Medico ")
    print("4 -> Agregar Paciente ")
    print("0 -> Salir ")

    opc = input("opcion >.. ")
    if opc == '1':
        print(pacientes)

    elif opc == '2':
        edadM()
    
    elif opc == '3':
        listaId()

    elif opc == '4':    
        agregaPaciente()


print("fin")

