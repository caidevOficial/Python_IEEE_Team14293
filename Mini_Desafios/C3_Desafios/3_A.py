# Obtener el promedio general sólo para aquellos alumnos 
# que aprobaron Matematica.

import pandas as pd 

rd = pd.read_excel("Datos.xlsx")

def aprobadosMatematica():
    aprobados = rd[rd["Matematica"]>=4]
    promedios = (aprobados["Matematica"] + aprobados["Quimica"] + aprobados["Fisica"])/3
    print(promedios)

# Test
aprobadosMatematica()