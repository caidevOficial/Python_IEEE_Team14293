# [B] Escribir una función que muestre todas las fichas para un juego de dominó como el anterior, 
#     en cualquier orden.
#     Llamar a las funciones anteriores con distintos valores para corroborar su funcionamiento
# EXAMPLE:
# mostrarFichas(3)
#   >>> 0-0
#   >>> 0-1
#   >>> 0-2
#   >>> 0-3
#   >>> 1-1
#   >>> 1-2
#   >>> 1-3
#   >>> 2-2
#   >>> 2-3
#   >>> 3-3

# Function [B]
def showTokens(number):
    atLeastOne = False
    for base in range(0,number+1):
        for sub in range(base,number+1): 
            print(f"Ficha: {base} - {sub}")
            atLeastOne = True
    return atLeastOne
    
# Test [B]
#mostrarFichas(3)

# Test Area
# Funcion [B]
#showTokens(3)