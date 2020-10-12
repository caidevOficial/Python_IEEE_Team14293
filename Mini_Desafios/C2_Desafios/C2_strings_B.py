# Para un desafío mayor: Si nombre_y_apellido cumple la restricción, 
# mostrar el nombre y apellido. En caso contrario nombre_y_apellido 
# debe valer la inicial del nombre y luego el apellido separado por 
# un espacio. Si todavía no se cumple la restricción entonces el valor 
# será la inicial del nombre y las primeras 24 letras del apellido. 
# Mostrar el nombre resultante.

def card():
    name = input("Ingrese nombre: ")
    surname = input("Ingrese apellido: ")

    nombre_y_apellido = name.capitalize() + " " + surname.capitalize()
    if(len(nombre_y_apellido)<=26):
        message = "Nombre admitido."
    else:
        message = "Nombre no admitido."
        nombre_y_apellido = name[0] + " " + surname
        if(len(nombre_y_apellido)>26):
            nombre_y_apellido = name[0] + " " + surname[0:24]

    validation = nombre_y_apellido
    print(message)
    print(validation)

# Test
card()