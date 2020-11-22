import pandas as pd 
# url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"

# Leo archivos.
df = pd.read_csv("full_data.csv")
pd.set_option("display.max_columns",10)
# Shape me devuelve el tamaño que tienen los datos - filas x columnas
print(df.shape)

# Size me devuelve la cantidad de celdas.
print(df.size)

