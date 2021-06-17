import math
import codecs
from operator import itemgetter
from statistics import mode

#Se crean las listas a llenar 
training = []
test = []
trainingLabels=[]
testLabels=[]

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
        distancias.append((distancia(testlist,traininglist),label))
        distancias.sort(key=itemgetter(0))
        votelabels=[]
        for x in distancias[:K]:
            votelabels.append(x[1])
        return mode(votelabels)

def get_k():
    while True:
        try:
            k = int(input('Escoge el valor de k (que sea impar): '))
            if k%2 != 0:
                return k
            elif k%2 == 0:
                while True:
                    result = input('El numero dado es par, desea continuar? (s/n): ')
                    result = result.lower()
                    result = result.strip()
                    if result == 's':
                        return k
                    elif result == 'n':
                        break
                    else:
                        print('Escribe "s" o "n"')
        except ValueError:
            print('Dato no valido')

#Cargar las bases de datos 
def load_data_base(k):
    print("Cargando archivo de entrenamiento")
    with codecs.open("training.txt","r","UTF-8") as file:
        for line in file:
            elementos=(line.rstrip('\n')).split(",")
            training.append([float(elementos[0]),float(elementos[1]),float(elementos[2]), float(elementos[3]),float(elementos[4]), float(elementos[5]), float(elementos[6]), float(elementos[7]), float(elementos[8]), float(elementos[9]), float(elementos[10]), float(elementos[11]),float(elementos[12])])
            trainingLabels.append(elementos[13])

    print("Cargando archivo de prueba")
    with codecs.open("test.txt","r","UTF-8") as file:
        for line in file:
            elements=(line.rstrip('\n')).split(",")
            test.append([float(elements[0]),float(elements[1]),float(elements[2]), float(elements[3]),float(elements[4]), float(elements[5]), float(elements[6]), float(elements[7]), float(elements[8]), float(elements[9]), float(elements[10]), float(elements[11]),float(elements[12])])
            testLabels.append(elements[13])

    print("Usando el sistema KNN en las muestras")
    prediccionescorrectas = 0
    prediccionestotales = 0
    for x,y in zip(test, testLabels):
        prediccionestotales += 1
        prediccion = clasificacion(x,training,trainingLabels,k)
        if prediccion == y:
            prediccionescorrectas += 1
        print(f'Prediction: {prediccion} etiqueta real: {y}')
    
     #Calculates model accuracy   
    print(f'Model accuracy: {round((prediccionescorrectas/prediccionestotales)*100,4)}%')

def run():
    load_data_base(get_k())

if __name__ == '__main__':
    run()