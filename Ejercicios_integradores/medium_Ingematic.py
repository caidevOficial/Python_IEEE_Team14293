# Escriba un programa que imprima los números del 1 al 100, 
# pero que para cada número que sea múltiplo de 3 imprima N3, 
# para los múltiplos de 5 imprima N5, y para los múltiplos de los dos, N3N5.
# Tips
# ¡Si el número es divisible por 3 entonces el resto de la división vale cero!

def ingematic():
    message = ""
    for i in range(1,100):
        message = "" # en cada iteracion lo seteo vacío
        if(i%3==0):
            message = "N3"
            if(i%5==0):
                message += "N5" # en este punto concatena ambos mensajes N3+N5
        elif(i%5==0):
            message = "N5"
        print(f"Number: {i} - {message}")

# Test
ingematic()