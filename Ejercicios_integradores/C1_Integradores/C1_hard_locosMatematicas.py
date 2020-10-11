def factorial(number):
    if number<=1:
        return 1
    else:
        return number*factorial(number-1)
    
def myPI(number): 
    multiply = 2**(3/2)/9801
    sumNumber = 0
    for k in range(number):
        sumNumber += factorial(4*k) /factorial(k)**4 *(1103+26390*k)/396**(4*k)
    return (1/(multiply*sumNumber))

print(myPI(10))