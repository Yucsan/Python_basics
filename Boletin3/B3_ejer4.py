"""
4. Queremos guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:

* La temperatura media de cada día. 
* Los días con menos temperatura. 

Se lee una temperatura por teclado 
y se muestran los días cuya temperatura máxima coincide con ella. 
si no existe ningún día se muestra un mensaje de información.
"""

dia1 = [12,15,10,16]
dia1.sort()
dia2 = [5,10,14,16]
dia2.sort()
dia3 = [12,15,10,17]
dia3.sort()
dia4 = [12,10,8,15]
dia4.sort()
dia5 = [6,11,17,13]
dia5.sort() # ya ordenados de menor a mayor

dias = [dia1,dia2,dia3,dia4,dia5] #lista de dias ya con temperaturas

hay = False
diasMax = []
diasMin = []

for i in dias:
    diasMax.append(i[-1]) #Maximas
    diasMin.append(i[0]) #Minimas

cuenta = 1 # indice del Día 

tempe = int(input("ingresa 1 temperatura"))

for i in diasMax:
    if i == tempe:
        print(f"el valor ingresado coincide con la Maxima del dia{cuenta}")
        hay = True

    cuenta +=1

if not hay:
    print("NO hay coincidencias")

#media
def temperaturaMedia(*args):
    media = (sum(args)) / len(args)
    return media

#muestro Temperaturas medias
for i, dia in enumerate(dias):
    print(f"la temperatura media del dia {i+1} es: {temperaturaMedia(*dia)} " )


#muestro 2 dia con temperaturas mínimas 
minima = list(diasMin) #dulplico el array
minima.sort()

for i,temp in enumerate(diasMin):
    if temp == minima[0]:
        print(f"la temperatura Minimas es {temp} del dia{i+1}")

    


