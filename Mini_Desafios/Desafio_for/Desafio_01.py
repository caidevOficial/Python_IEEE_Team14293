# Mostrar la siguiente secuencia de datos utilizando 
# la instrucción for y la instrucción if:
# 0, 1, 4, 9, 16, 25, 6, 7, 8, 9

numberPrinted = 0

for i in range(1,14,2):
    if(numberPrinted < 26):
        print(numberPrinted)
        numberPrinted += i # le sumo los valores de i: 1,3,5,7,9
    else: # Cuando numberPrinted supera el 25, imprimo de 6 a 9
        for n in range(6,10):
            print(n)


