# Realizar un programa que pida al usuario un número de legajo y 
# el nombre completo, luego lo guarde en un diccionario.
# Usar dos celdas de codigo, en una crear el diccionario, 
# y en la otra agregar el nombre y legajo, mostrar el contenido. 
# La idea es que cuando se ejecute varias veces la segunda celda se 
# agrege un nuevo nombre y legajo a lo que ya había sido almacenado en el diccionario.

def chargeDictionary():
    for ite in range(0,3):
        key = int(input(f"Ingrese {ite+1}° legajo: "))
        content = input("Nombre: ")
        if key not in dic.values():
            # TODO arreglar el if, si existe, lo agrega igual, tapando el contenido anterior
            dic[key] = content
        else:
            print("Ya existe esa key.")
    print(dic)

# Test
dic = {}
print(dic)

chargeDictionary()