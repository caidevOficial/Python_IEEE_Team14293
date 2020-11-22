# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. 
# El archivo tiene dos columnas, Equipo y Puntos. 
# Determinar de cada equipo la diferencia de gol 
# (goles a favor - goles en contra), y mostrar todas las diferencias 
# de gol con print
import pandas as pd 

rd = pd.read_excel("Tabla1.xlsx")
#print(rd)

def goalDifference(goalFav, goalCon):
    difference = 0
    if (goalFav>0 and goalCon>0):
        difference = goalFav - goalCon
    return (difference)

def setGoalDifference():
    equiposDict = rd.to_dict("records")
    key = "Diferencia"
    goles_diferencia = 0
    for equipo in equiposDict:
        goles_diferencia = goalDifference(equipo["Goles a favor"], equipo["Goles en contra"])
        equipo[key] = goles_diferencia
    df = pd.DataFrame(equiposDict)
    print((df))

# Test
setGoalDifference()