# A pesar de que el domino tradicional se juega con fichas 
# hasta el número 6, vamos a considerar un juego de fichas 
# de valor máximo  n .
# [A] Escribir una función que calcule la cantidad de fichas 
#     para un juego de dominó completo con fichas que contienen 
#     hasta el número n. 
#     Nota: 
#     [1] ¡No hay fichas repetidas! 
#     [2] 2-4 es la misma ficha que 4-2. 
#     [3] ¡Observar que en el dominó hay fichas con valor 0!
# EXAMPLE:
# cantidadFichas(3)
#   >>> 10
#   cantidadFichas(4)
#   >>> 15

# Function [A]
def amountOfTokens(number):
    amountLessTokens = 0
    for f in range(0,number+1):
        amountLessTokens += f
    amount = (number+1)*(number+1) - (amountLessTokens)
    return amount

# Test [A]
def testA(var):
    tokens = amountOfTokens(var)
    print(f"Cantidad de fichas con el {var}: {tokens}")

# TEST AREA
# Funcion [A]
testA(4)

