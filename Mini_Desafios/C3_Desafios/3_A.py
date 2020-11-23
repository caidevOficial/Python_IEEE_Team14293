# Obtener el promedio general sólo para aquellos alumnos 
# que aprobaron Matematica.

import pandas as pd 

rd = pd.read_excel("Datos.xlsx")

def aprobadosMatematica():
    aprobados = rd[rd["Matematica"]>=6]
    promedios = (aprobados["Matematica"] + aprobados["Quimica"] + aprobados["Fisica"])/3
    prom_gral = sum(promedios)/len(promedios)
    print(prom_gral)

# Test
aprobadosMatematica()