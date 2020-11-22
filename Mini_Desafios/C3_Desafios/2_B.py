# Escribir una funcion que reciba como parámetros: 
# una variable de tipo DataFrame (la tabla de alumnos) 
# y el índice de un alumno. Luego debe devolver con return 
# el promedio de sus notas en las diferentes materias.

import pandas as pd 

rd = pd.read_excel("Datos.xlsx")
# Example
# index = 2
# alumno = rd.loc[index]
# print(alumno["Quimica"])

def makeOveral2(df,index):
    index = int(index)
    df = pd.DataFrame(df)
    student = df.loc[index]
    sum_notes = int(student["Quimica"]) + int(student["Matematica"]) + int(student["Fisica"])
    overall = sum_notes/3
    print(overall)
    return overall

# Test
makeOveral2(rd,2)
