# Ordenar palabras
# Std input:
# n palabras separadas por espacios
# Output deseado:
# Una lista de palabras ordenadas alfabeticamente enseparadas por newlines.
# Recomendación: Investigar el método sort para ordenar y split para separar 
# un string y convertirlo a una lista.
# Ejemplo:
# Input:
# saludos al gran rey
# Salida del programa (lo que se imprime):
# al
# gran
# rey
# saludos
# Suponga que la entrada es toda en minusculas
# Se recomienda usar el método .split() sin argumentos para colimar 
# el espacio en blanco. Ver stack overflow para entender la diferencia 
# entre split con o sin argumentos.

string = "ohayou sekai good morning world"

def Ordenar(cadena):
    arrayPalabras = cadena.split()
    arrayPalabras.sort()
    for palabra in arrayPalabras:
        print(palabra)

# Test
Ordenar(string)

