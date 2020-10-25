# Crear una lista con los números pares menores a 50.

def pairsNumbersTill50():
    newList = []
    for number in range(0,50):
        if(number%2==0):
            newList.append(number)
    print(newList)

# Test
pairsNumbersTill50()