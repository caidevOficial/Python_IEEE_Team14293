# El número  e  tiene inmensa utilidad para el análisis y la estadística, 
# es una de las super-estrellas de la matemática, y su utilidad radica en que la función  
# ex  es igual a su derivada, por definición de  e .
# Gracias a las series de Taylor podemos obtener la siguiente definición del número  e :
# e=1 + 1/1! + 1/2! + 1/3! + 1/4! + 1/5!+... 
# 
# Se pide obtener una aproximación del número e calculando la suma de los primeros 
# 20 términos de esta sucesión infinita.
# Tips
# n!=1⋅2⋅3⋅ ... ⋅n .

# Defino funcion factorial
def factorial(number):
    if number <= 2:
        return number
    else:
        #number = long (number)
        facto = (number * factorial(number-1))
        return facto

# Defino funcion numero de Euler
def e_stimation():
    eValue = 1
    for value in range(1,21):
        eValue += (1/factorial(value))
    print(f"Euler 20 terminos: {eValue}")

e_stimation()
