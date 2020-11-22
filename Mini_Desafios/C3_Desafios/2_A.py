# Calcular el promedio de las notas de química de todos los 
# alumnos en el archivo Datos.xlsx.
# Tip: Podemos usar la función sum( iterable ) para obtener 
# la suma de todos los campos. Un ejemplo de como funciona:

import pandas as pd 

rd = pd.read_excel("Datos.xlsx")

def makeOveral():
    total = sum(rd["Quimica"])
    counter = len(rd)
   
    if(counter>0):
        overal = total/counter
    else:
        overal = 0
    print(f"Promedio: ", overal)

# Test
makeOveral()
