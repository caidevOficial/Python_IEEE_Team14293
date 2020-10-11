# Escribir una función que recibe un numero y devuelve True 
# si el numero es primo y False en caso contrario.
# Mediante un for verificar la primalidad de los numeros del  1  al  20 .
# Tips
# Un número  N  es primo cuando tiene exactamente  2  divisores ( 1  y  N ). 
# Sin embargo alcanza con verificar que no es múltiplo de ningún 
# número entre  2  y  N−−√  (recordar que  N−−√=N0.5 )
# El numero 1 no es primo.

def isPrime(var):
    primeNumber = True
    
    if(var<2):
        primeNumber = False # menor a 2, no es primo
    else:
        if(var<5):
            number = var # itero hasta el numero ingresado
        else:
            number = int(var/2) # para iterar hasta la mitad del numero
    for i in range(2,(number)): # rango entre 2 y el numero ingresado
        if(var%i==0): # Voy chequeando que sea divisor
            primeNumber = False
    return primeNumber

# Test
numero = 7
print(f"El numero {numero} es primo? : {isPrime(numero)}")