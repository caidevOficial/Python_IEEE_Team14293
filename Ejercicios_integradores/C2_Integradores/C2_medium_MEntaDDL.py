# Volviendo de hacer las compras en el supermercado, pasas cerca de una heladería y 
# decidís comprar helado para tus hermanos, los cuales son amantes de la menta granizada 
# y del dulce de leche con nuez. El negocio ofrece helado en todo tipo de formato, desde 
# mini-cucuruchos hasta potes de 1 kilo, y cada formato cuesta cierta cantidad de dinero. 
# Decidís gastar exactamente todo el dinero que te queda luego de haber ido al supermercado, 
# de forma tal que no sobre ni falte.

# Programar una función que recibe una lista con los precios de los distintos formatos en 
# que se vende el helado, y además reciba la cantidad de dinero disponible para gastar. 
# La función debe encontrar la manera de comprar cierto formato de helado sabor menta, y 
# cierto formato sabor dulce de leche, de manera de gastar la totalidad del dinero disponible. 
# En consecuencia, la cantidad de formatos seleccionados debe ser exactamente 2, está permitido 
# seleccionar el mismo formato para ambos sabores de helado. La función debe devolver con return 
# una lista de 2 elementos, los cuales serán los precios de los formatos de helado seleccionados. 
# En caso de no existir una combinación que satisface los requisitos se debe devolver [-1, -1].

# Tips:
# Al usar un set o un diccionario como estructura de datos pueden mejorar la velocidad con la 
# que el programa analiza si cierto elemento se encuentra dentro de los datos. La operación 
# mi_set = set( mi_lista ) puede serles de utilidad para este propósito.
# Ejemplos
# buscar_precios( [1, 2, 3, 4, 5] , 8) => [3, 5]
# buscar_precios( [7, 4, 2, 6, 7, 7] , 4) => [2, 2]
# buscar_precios( [4, 3, 7, 5] , 5) => [-1, -1]

precios = {2,4,6,8,10}

def combinacion(precio,number):
    lista = []
    for i in precio:
        for j in precio:
            if(i+j == number):
                lista.append(i)
                lista.append(j)
                return lista # retorno lista con 2 elementos
    lista = [-1,-1] # si no hay, retorno esto
    return lista

# Test
list = []
list = combinacion(precios,16)
print(list)