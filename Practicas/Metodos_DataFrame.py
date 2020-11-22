import pandas as pd 
# url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"

# Leo archivos.
df = pd.read_csv("full_data.csv")
pd.set_option("display.max_columns",10)
print(df.shape)

# sum y max
suma = (df["new_cases"].sum() / 2)
maximo = df["total_cases"].max()
print(suma,maximo)

# Info me devuelve el tipo de dato de cada columna.
print(df.info())