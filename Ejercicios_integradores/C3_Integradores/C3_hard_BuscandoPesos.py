# Utilizando el set de datos del archivo california_housing_train.xlsx
# Dividir el area cubierta por el censo en cuadrantes de 
# 0.5 de latitud x 0.5 de longitud, encontrar para qué 
# cuadrante el valor medio de 'median_house_value' es máximo. 
# Asignar el paso como una variable para que pueda cambiarse facilmente. 
# Para filtrar las zonas de muy baja residencia descarten los valores 
# cuando hay menos de 100 casas

# Datos utiles:
# Minimo de longitud: -124.3
# Máximo de longitud: -114.3
# Minimo de latitud: 32.5
# Máximo de latitud: 42.5
# Tips: El programa va a tardar en correr, 
# no se asusten! Pueden investigar funciones 
# de numpy para ayudarlos a resolver el problema 
# numpy.arange.
# Nota final: Busquen en el mapa estas coordenadas 
# para ver donde quedan!

import pandas as pd
import numpy as np

archivo = pd.read_excel("california_housing_train.xlsx") 

paso = .5
# Setear latitud
latitude = [32.5,42.5]
# Setear longitud
longitude = [-124.3,-114.3]

rangoLats = np.arange(latitude[0],latitude[1],paso)
rangoLons = np.arange(longitude[0],longitude[1],paso)

# Seteo la matriz
maximaLat = len(rangoLats)
maximaLon = len(rangoLons)
maximoValor = np.zeros((maximaLat, maximaLon))
# Para probar la matriz
#maximoValor[0][0]=1 # Matriz
# print(maximoValor)
# exit()

for casa in range(archivo.shape[0]):
    valor = archivo.iloc[casa]["median_house_value"]
    lat,lon = archivo.iloc[casa]["latitude"], archivo.iloc[casa]["longitude"]
    # itero los indices de longitud
    for lo in range(maximaLon-1):
        if lon >= rangoLons[lo] and lon< rangoLons[lo+1]:
            break
    # itero los indices de latitud
    for la in range(maximaLat-1):
        if lat >= rangoLats[la] and lat< rangoLats[la+1]:
            break
    if maximoValor[la][lo] < valor:
        maximoValor[la][lo] = valor
print(maximoValor)
