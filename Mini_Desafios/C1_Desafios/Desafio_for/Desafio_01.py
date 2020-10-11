# Mostrar la siguiente secuencia de datos utilizando 
# la instrucción for y la instrucción if:
# 0, 1, 4, 9, 16, 25, 6, 7, 8, 9

numberPrinted = 0

for i in range(1,10):
    if(i < 6):
        numberPrinted = i**2
        print(numberPrinted) # Imprimo i al cuadrado
    else:
        print(i)


