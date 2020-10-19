# Se recibieron distintos postulantes para un empleo de traductor. 
# Crear un diccionario en el cual la clave de cada elemento sea el nombre 
# de un candidato y el contenido sea un diccionario de los idiomas que aprendió. 
# Para armar el diccionario de idiomas de cada candidato, los elementos deben tener 
# como clave el nombre del idioma y como contenido el valor True o False para los 
# siguientes idiomas: Español, Ingles, Chino, Frances, Italiano.
# Ejemplo del diccionario de idiomas:
# {"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True}
# Inventar valores para 5 candidatos.
# El usuario luego debe poder ingresar el nombre de un idioma y el programa deberá 
# mostrar en pantalla el nombre de aquellos candidatos que aprendieron ese idioma.

def newDictionary(dictionaryBase):
    for charge in range(0,5):
        key = input("Ingrese nombre: ")
        content = dictionaryBase[charge]
        if key not in dic.values():
            dic[key] = content
            #print("asd")
        else:
            print("key duplicado")
    print(dic)


#TODO arreglar, no funciona.
# Test
dic = {}

dic2 = {
    #{"Español":True, "Ingles":True, "Chino":True, "Frances":False, "Italiano":False},
    #{"Español":True, "Ingles":False, "Chino":True, "Frances":False, "Italiano":False},
    #{"Español":True, "Ingles":True, "Chino":True, "Frances":True, "Italiano":True},
    #{"Español":True, "Ingles":False, "Chino":False, "Frances":False, "Italiano":False},
    {"Español":False, "Ingles":False, "Chino":True, "Frances":False, "Italiano":False}
}

newDictionary(dic2)
print(dic)