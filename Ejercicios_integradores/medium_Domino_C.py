# [C] Escribir una función que, dada una cantidad de fichas, calcule cuál es el n (valor máximo) 
#     de las fichas. Si el número de fichas no corresponde a la cantidad de fichas de ningún 
#     juego de dominó completo retornar -1.
# EXAMPLE:
# valorMaximo(10)
#   >>> 3
#   valorMaximo(11)
#   >>> -1
import medium_Domino_A 
# Ruta del modulo con la funcion a utilizar, pa no repetir, vió? :v

# Function [C]
def maxValueOfTokens(number):
    maxValue = -1 # Valor a retornar si hay error.
    amountOfTokens = 0 # Contados de fichas.
    iterator = 0 # Numero iterador para saber la ficha maxima.
    while(amountOfTokens<number):
        # cuento las cantidades de fichas segun la iteracion
        amountOfTokens = medium_Domino_A.amountOfTokens(iterator)
        iterator += 1
    # Si mi cantidad coincide con las pasadas por parametro
    # Actualizo con el numero iterador y lo retorno.
    if(amountOfTokens==number):
        maxValue = (iterator-1)
    return maxValue


# Test [C]
cantidad = maxValueOfTokens(22)
print(f"Ficha maxima es: {cantidad}")