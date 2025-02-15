"""
3.- Crea un programa que permita introducir a un profesor las notas de sus estudiantes 
(máximo 10 estudiantes). Los datos se deberán almacenar en un diccionario como el siguiente:

estudiantes = 	{"1": {"nombre": "Lorena","nota": 8},
"2": {"nombre": "Markel","nota": "4.2"},
"3": {"nombre": "Julen","nota": 6.5}}

Una vez introducidos todos los datos, 
el programa mostrará una lista con los nombres de los estudiantes 
que han suspendido y otra con los que han aprobado. 
También calculará y mostrará la nota media de la clase

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


