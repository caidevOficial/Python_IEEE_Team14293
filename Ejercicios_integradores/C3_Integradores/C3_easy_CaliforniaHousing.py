# Este archivo contiene un conjunto de datos de viviendas de 
# California, el cual fue extraido del censo de nacional de 1990. 
# Para mas info sobre el set de datos: 
# https://developers.google.com/machine-learning/crash-course/california-housing-data-description
# Extraer la siguiente información:
# [1] - ¿Cuantas casas hay con valor 'median_house_value' 
# mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
# [2] - ¿Cual es el promedio de habitaciones por manzana ('total_rooms') 
# de estas casas? Rta: 2466.31
# [3] - ¿Cual es la casa más cara? ¿Cuántas hay con este valor? 
# Rta: 500001.0 - 814
# ★★ CHALLENGE: Obtener la media y la varianza de la propiedad 
# 'median_house_value'. Rta: 207300.91 - 13451442293.57
# Tip: ¡Pueden investigar funciones de numpy para conseguir la media y la varianza! numpy.var

import pandas as pd 
link = "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_3_datos/california_housing_train.xlsx"

# setear columnas
pd.options.display.max_columns = 10
df = pd.read_excel("california_housing_train.xlsx")

# [1]
def exersise1(df):
    df1 = df[ (df["median_house_value"]>80000) & (df["longitude"]<= -118.0) & (df["longitude"]>= -120.0)]
    return df1

# [2]
def exersise2(df1):
    total = df1["total_rooms"].mean()
    # devuelve el promedio
    return total

# [3]
def exersise3_A(df):
    maxValue = df["median_house_value"].max()
    return maxValue

def exercise3_B(df,maxValue):
    totalHouses = df[df["median_house_value"] == maxValue].shape[0]
    return totalHouses


# Test
df1 = exersise1(df)
print("Exercise 1:")
print(df.shape, df1.shape)

total = exersise2(df1)
print("Exercise 2:")
print("Total: ", total)

max = exersise3_A(df)
totalHouse = exercise3_B(df,max)
print("Exercise 3_A:")
print("Max value: ", max)
print("Exercise 3_B:")
print("Total Houses: ", totalHouse)
