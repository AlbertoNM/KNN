import math
import codecs
from operator import itemgetter
from statistics import mode

# Definimos la función de distancia euclidiana 
def distancia(lista1,lista2):
    sumatoria=0
    for x,y in zip(lista1,lista2):  # con el zip se van a juntar las coordenadas x de la lista uno con las coordenadas x de la lista 2 y lo mismo para y
        sumatoria +=  (x-y) ** 2
    return math.sqrt(sumatoria)

# Definir la función de clasificación 
def clasificacion(testlist,traininglist,traininglabel,K):
    distancias = []
    for traininglist, label in zip(traininglist,traininglabel):
        distancias.append(distancia(testlist,traininglist),label)
        distancias.sort(key=itemgetter(0))
        votelabels=[]
        for x in distancias[:K]:
            votelabels.append(x[1])
        return mode(votelabels)

#Se crean las listas a llenar 
training = []
test = []
trainingLabels=[]
testLabels=[]

while True:
  try:
    k = int(input('Escoge el valor de k (que sea impar): ')
    break #siempre debe ser un numero imprar para que funcione 
  except ValueError:
    print('No es un numero')