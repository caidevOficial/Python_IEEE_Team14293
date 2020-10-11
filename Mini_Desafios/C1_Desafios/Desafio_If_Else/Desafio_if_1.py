# Realizar un programa que revise si una nota está aprobada 
# (es decir si es mayor o igual a 4) utilizando un if/else. 
# La nota será ingresada por el usuario usando input()

nota = int(input("Ingrese una nota [1-10]: "))
mensaje = ""

if(nota>=4):
    mensaje = "Aprobado!"
else:
    mensaje = "Desaprobado"

print(mensaje)