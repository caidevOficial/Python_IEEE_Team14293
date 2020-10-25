# Realizar un programa que pida al usuario un número de legajo y 
# el nombre completo, luego lo guarde en un diccionario.
# Usar dos celdas de codigo, en una crear el diccionario, 
# y en la otra agregar el nombre y legajo, mostrar el contenido. 
# La idea es que cuando se ejecute varias veces la segunda celda se 
# agrege un nuevo nombre y legajo a lo que ya había sido almacenado en el diccionario.

def chargeDictionary():
    dic = {}
    for ite in range(0,3):
        key = int(input(f"Ingrese {ite+1}° legajo: "))
        if key in dic.values():
            print("Ya existe esa key.")
        else:
            content = input("Nombre: ")
            dic[key] = content
            # TODO arreglar el if, si existe, lo agrega igual, tapando el contenido anterior
    return dic

# Test
diccionario = {}
print(diccionario)

diccionario = chargeDictionary()
print(diccionario)