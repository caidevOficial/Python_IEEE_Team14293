import pandas as pd
from pandas._config.config import set_option 
# url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"

# Leo archivos.
df = pd.read_csv("full_data.csv")
pd.set_option("display.max_columns",10)

# df[d["col"]>100]
# df[d["name"]>"N" | d["Quimica"]>21]

# Seteo la locacion del dataFrame a un pais especifico
df = df[df["location"]!="Argentina"]

# Filtro el dato con el numero maximo de casos que hubo
seleccion = df[df["new_cases"] == df["new_cases"].max()]
print(seleccion)
