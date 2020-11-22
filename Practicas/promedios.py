import pandas as pd 

rd = pd.read_excel("Datos.xlsx")

promedios = (rd["Quimica"] + rd["Fisica"] + rd["Matematica"])/3
print("Promedios:")
print(promedios)
print("El promedio maximo es: ", promedios.max())

# Podemos ver que cuando se suman columnas de un DataFrame, 
# se calcula la suma elemento a elemento, como si hiciera la 
# operación suma para cada fila por separado. Cuando se divide 
# por 3 la suma de las columnas, realiza la división por 3 de cada 
# resultado por separado y queda al final 1 resultado por fila. 
# Esto es muy práctico y también funciona con otros operadores.