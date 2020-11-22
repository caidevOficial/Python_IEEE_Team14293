import pandas as pd 
# url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
# Leo archivos.
df = pd.read_csv("full_data.csv")

# con set_option seteo el display, poniendo columnas maximas = 10
pd.set_option("display.max_columns",10)
