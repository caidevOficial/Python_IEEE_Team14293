# UNE Y TRIUNFARAS
# Se recibieron distintos postulantes para un empleo de traductor. 
# Crear un diccionario en el cuál la key de cada elemento sea el nombre 
# de un candidato y el contenido sea un set con los idiomas que aprendió. 
# Inventar valores para 5 candidatos.
# Mostrar en pantalla los idiomas que todos los candidatos aprendieron.
# Mostrar en pantalla todos los candidatos que aprendieron por lo menos Español e Inglés.
# El usuario luego debe poder ingresar el nombre de un idioma y el programa 
# deberá mostrar en pantalla el nombre de aquellos candidatos que aprendieron ese idioma.

idiomas = [
    ["español", "ingles", "chino", "japones"],
    ["español", "ingles", "chino"],
    ["español", "ingles", "japones"],
    ["español", "chino", "japones"],
    ["ingles", "chino", "japones"]
]

def traductor(idiomas):
    dic = {}
    for i in range(0,5):
        key = input("nombre: ")
        content = idiomas[i]
        if key not in dic.values():
            dic[key] = content
    return dic

# Test
dic2 = traductor(idiomas)
print(dic2)