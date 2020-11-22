# Leer el archivo Tabla1.xlsx que contiene los puntos de 
# un campeonato y determinar qué equipo es el campeón (1ro) 
# y perdedor (último). El archivo tiene dos columnas, Equipo y Puntos

import pandas as pd 

rd = pd.read_excel("Tabla1.xlsx")

def findChampion():
    champion = {}
    points = 0
    teams = rd.to_dict("records")

    for team in teams:
        if((team["Puntos"]) > points):
            champion = team
            points = (team["Puntos"])
    return(champion)

def findLoser():
    loser = {}
    points = 500
    teams = rd.to_dict("records")

    for team in teams:
        if((team["Puntos"]) < points):
            loser = team
            points = (team["Puntos"])
    return(loser)

def ChampionAndLoser():
    champ = findChampion()
    loser = findLoser()
    print(f"Campeon: ", champ)
    print(f"Ultimo: ",loser)

# Test
ChampionAndLoser()
