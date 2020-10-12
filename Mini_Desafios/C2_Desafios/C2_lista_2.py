# Crear una lista con el nombre de los días de la semana. 
# Realizar un programa al cual se ingresa el día del año mediante 
# un número de 0 a 364, que determine a qué día de la semana corresponde 
# mediante un número de 0 (Lunes) a 6 (Domingo) y luego muestre en 
# pantalla el elemento correspondiente de la lista, o sea, el día de la 
# semana en forma de texto (suponemos que el día 0 del año es Lunes).
# Ejemplos:
# calcularDia(1) => 'Martes' (Ya que el día 0 es Lunes)
# calcularDia(10) => 'Jueves' (Ya que el día 7 también es Lunes)

def calcularDia(number):
    days = ["Lunes", "Martes", "Miercoles", 
    "Jueves", "Viernes", "Sabado", "Domingo"]

    indexDay = number%7
    print(f"El dia corresponde a: {days[indexDay]}")

# Test
numberDay = int(input("Ingrese un dia del año entre [0-364]: "))
calcularDia(numberDay)