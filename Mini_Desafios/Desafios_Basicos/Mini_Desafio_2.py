# Realizar un programa al cual se ingresa el día del año mediante un 
# número de 0 a 364, y que muestra en pantalla a qué día de la semana 
# corresponde mediante un número de 0 a 6 (mostrar el número 0 si corresponde 
# a Lunes y 6 si es Domingo)
# Suponemos que el día 0 del año cae un Lunes.
# Pista (seleccionar texto para ver): 
# Los días múltiplos de 7 corresponden a 0 (Lunes), 
# los días que tienen resto 1 en la división por 7 corresponden a 1 (Martes), 
# los días que tienen resto 2 en la división por 7 corresponden a 2 (Miércoles), 
# etc.

dia = int(input("Ingrese un dia del año: "))
resto = dia%7
dia = ""

if(resto==0):
    dia = "Lunes"
elif(resto==1):
    dia = "Martes"
elif (resto==2):
    dia = "Miercoles"
elif(resto==3):
    dia = "Jueves"
elif(resto==4):
    dia = "Viernes"
elif(resto==5):
    dia = "Sabado"
elif (resto==6):
    dia = "Domingo"

print("El dia corresponde a: ")
print(dia)
