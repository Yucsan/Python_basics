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

estudiantes = {}
alumno = {}

for i in range(2):
    nombre = input('inserta un nombre: ')
    nota = input('inserta nota: ')
    alumno['nombre'] = nombre
    alumno['nota'] = int(nota)
    estudiantes[i] = alumno
    alumno = {}

print("APROBADOS")
for i in estudiantes:
    if estudiantes[i]['nota'] > 4:
        print(estudiantes[i])

print("DESAPROBADOS")
for i in estudiantes:
    if estudiantes[i]['nota'] < 5:
        print(estudiantes[i])

#print(estudiantes)

print("fin")


