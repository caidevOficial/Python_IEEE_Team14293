import pandas as pd 

file = pd.read_excel("Datos.xlsx")
print(file)

# Se puede dar el nombre de la columna como indice
file2 = pd.read_excel("Datos.xlsx", index_col="Legajo")
print(file2)

# tambien se puede dar el numero de indice
file3 = pd.read_excel("Datos.xlsx", index_col=0)
print(file3)

# esto permite acceder con .loc mediante legajo
print(file2.loc[35679])