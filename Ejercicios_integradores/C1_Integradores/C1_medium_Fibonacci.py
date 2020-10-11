# Imprima  n  números de la sucesion de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacciCalculus(number):
    initialNumber = 0
    initialSecondNumber = 1
    fiboNumber = 0
    counterIterator = 0

    while(counterIterator < number):
        print(f"{counterIterator+1}° Numero: {fiboNumber}")
        initialNumber = initialSecondNumber
        initialSecondNumber = fiboNumber
        fiboNumber = initialNumber + initialSecondNumber
        counterIterator += 1

# Test
fibonacciCalculus(100)