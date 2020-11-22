f = open('noticia.txt', encoding='utf-8')
texto = f.read()

# separar por palabras y contar cuantas veces aparece

# Proceso el texto deshaciendome de lo que no quiero
# Opcion 1
# texto = texto.replace("’s","")
# texto = texto.replace("—","")

# Opcion 2 y mas eficiente
reemplazar = ['’s','—',',','.','\n','\ufeff']
for indeseado in reemplazar:
    texto = texto.replace(indeseado,' ')

# Convierto texto en lista
palabras = texto.split(' ')

# Hago diccionario para contar ocurrencias
ocurrencias = {}

for palabra in palabras:
    palabra = palabra.lower()
    if palabra != '':
        if palabra not in ocurrencias:
            ocurrencias[palabra] = 1
        else:
            ocurrencias[palabra] += 1
# print(ocurrencias['the'])

# Convierto el diccionario en lista de keys.
lista = list(ocurrencias.keys())

# Se crea una funcion que retornara el contenido de la clave
def miFuncion(clave):
    return ocurrencias[clave]

# Se la paso al sort junto con el parametro desendente
lista.sort(reverse=True,key=miFuncion)
print(lista)