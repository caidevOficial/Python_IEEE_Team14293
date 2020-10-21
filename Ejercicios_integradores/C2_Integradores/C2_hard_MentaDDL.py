#  Modificar la función para que el resultado sea 1 sólo número: 
# La cantidad de maneras diferentes de conseguir el objetivo 
# (si dos formatos tienen el mismo precio, igualmente califican como formatos diferentes).

precios = {2,4,6,8,10}

def combinacion(precio,number):
    lista = []
    quantity = 0
    for i in precio:
        for j in precio:
            if(i+j == number):
                lista.append(i)
                lista.append(j)
                quantity += 1
    return quantity

# Test
list = []
list = combinacion(precios,8)
print(list)