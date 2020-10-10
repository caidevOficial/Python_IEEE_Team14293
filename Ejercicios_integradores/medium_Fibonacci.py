# Imprima  n  números de la sucesion de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacciCalculus():
    initialNumber = 0
    prevNumber = initialNumber
    for i in range(0,18):
        if(i<2): # imprimo 0 y 1, guardo los valores en variables
            fiboNumber = prevNumber + i
            beforePrevNumber = prevNumber
            prevNumber = fiboNumber
        else:
            # EL numero fibo es igual a la suma del ultimo + el  penultimo Fibo
            fiboNumber = prevNumber + beforePrevNumber
            # El ultimo fibo, pasa a ser el penultimo fibo mostrado
            beforePrevNumber = prevNumber
            # el actual fibo, pasa a ser el ultimo fibo mostrado
            prevNumber = fiboNumber
        print(fiboNumber) # imprimo el fibo actual

# Test
fibonacciCalculus()