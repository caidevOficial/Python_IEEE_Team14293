# #### Mini-desafío If y While
# Implementar un programa que muestre la siguiente secuencia:
# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0
# **Para un desafío mayor:** Utilizar un solo *while*, un solo *if* 
# y un solo *else*

ascendente = True
contador = 1

while contador>0:
    print(contador)
    if contador<5 and ascendente:
        contador = contador + 1
    else:
        ascendente = False
        contador = contador - 1
    