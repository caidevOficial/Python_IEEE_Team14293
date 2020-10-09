# Cálcular la nota de un alumno es una tarea cotidiana de un profesor. 
# Esta tarea suele realizarse a mano o en excel muchas veces. 
# En esta ocasión la haremos en python.
# Escribir una función que calcule el promedio de 3 notas y 
# entrege ese valor usando return.
# Reescribir la función anterior modificandola para asignar una 
# importancia al primer examen de 20%, al segundo de 50% y al tercero de 30%.
# Llamar a cada función anterior 3 veces con distintas notas y 
# verificar, mediante la instrucción if, si el alumno aprobó 
# en cada caso (suponga que 4 es la nota de aprobación).

def calificationAverage(note1, note2, note3):
    sumNotes = note1 + note2 + note3
    return sumNotes/3

def calificationAverageImportance(note1, note2, note3):
    sumNotes = (note1*0.2)+(note2*0.5)+(note3*0.3)
    return sumNotes

# Pruebas de código
finalNote1 = calificationAverage(10,1,10)
print(f"Promedio: {finalNote1}")
finalNote1 = calificationAverageImportance(10,1,10)
print(f"Promedio: {finalNote1}")