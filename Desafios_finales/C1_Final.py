# La conjetura del Dr. Lothar
# Escriba un programa que reciba un numero del usuario 
# y repita el siguiente proceso usando un while:
# Si el numero es par, se debe dividir por  2 .
# Si el numero es impar, se debe multiplicar por  3  y sumar  1 .
# Este proceso se repite hasta llegar al numero  1  y luego muestra 
# en pantalla la cantidad de pasos que tardó en llegar.

# Ejemplo para  n=6 :
# 6,3,10,5,16,8,4,2,1 
# Resultado = 8

def drLothar():
    number = int(input("Escribe un numero: "))
    stepsCounter = 0
    while(number>1):
        if(number%2==0):
            number /= 2
        else:
            number = (number * 3) + 1
        stepsCounter += 1
    return stepsCounter

# Test
steps = drLothar()
print(f"Cantidad de pasos: {steps}")