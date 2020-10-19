# Imprima  n  números de la sucesion de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacciCalculusRec(n):
    if(n==0 or n==1):
        return n
    else:
        return (fibonacciCalculusRec(n-1) + fibonacciCalculusRec(n-2))

# Test
numero = fibonacciCalculusRec(12)
print(numero)