import pandas as pd 

# Ejemplo 1 - Leo datos de un archivo
df = pd.read_excel("Datos.xlsx")
# guardo una tupla en mariable
alumno = df.loc[0]
print(alumno) # imprimo la tupla especificada.
print(df) # imprimo la lista entera

# Ejemplo 2
d = df.to_dict("list") # me trae un diccionario y las keys son los nombres de las columnas
# muy util para procesar todos los datos de uan columna
print(d)

# Ejemplo 3
# muy util para buscar algo puntual, un nombre por ejemplo.
d2 = df.to_dict("records") # lista con varios dicc adentro (info de cada fila)
#print(d2)
for alumno in d2:
    if alumno["Nombre"] == "Sol":
        print("Te encontre: ",alumno)

dfindex = pd.read_excel("Datos.xlsx", index_col="Legajo")
print(dfindex)