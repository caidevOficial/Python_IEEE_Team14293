# Realizar un programa que ordena nombres alfabeticamente. 
# Primero debe pedir al usuario que ingrese el número de nombres 
# que serán ingresados, luego debe pedir al usuario que ingrese un 
# nombre y repetir ese pedido la cantidad de veces indicada. 
# Los nombres se deben ir agregando a una lista. Por último, ordenar 
# la lista alfabéticamente y mostrar en pantalla de a uno por vez los 
# nombres ordenados (usando un for).

def takeAndSort():
    amountNames = int(input("Ingrese cantidad de nombres: "))
    names = []
    # pido nombres y guardo en los indices
    for index in range(0,amountNames):
        names.append(input(f"Ingrese el {index+1}° nombre: "))
    # ordeno alfabeticamente
    names.sort()
    #muestro ordenados
    for name in names:
        print(name)

# Test
takeAndSort()
