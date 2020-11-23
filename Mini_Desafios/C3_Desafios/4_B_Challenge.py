# Encontrar la palabra con mayor numero de ocurrencias 
# en el texto de la noticia.
link = 'noticia.txt'

def openText(link):
    f = open(link, encoding='utf-8')
    texto = f.read()
    return texto # devuelvo el texto abierto

def replaceCharacters(texto):
    reemplazar = ['’s','—',',','.','\n','\ufeff']
    for indeseado in reemplazar:
        texto = texto.replace(indeseado,' ')
    return texto # devuelvo el texto sin los caracteres especificados

def dictionaryOcurrences(palabras):
    # Hago diccionario para contar ocurrencias
    ocurrencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra != '' and (palabra=='trump' or palabra=='the'):
            if palabra not in ocurrencias:
                ocurrencias[palabra] = 1 # si la palabra no esta en el diccionario, seteo en 1 su valor
            else:
                ocurrencias[palabra] += 1 # si est en el dicc, sumo 1 a su valor
    return ocurrencias # retorno el diccionario palabra:ocurencias

def biggerOcurrence(ocurrencias):
    maximaCantidad = 0
    mayorOcurrencia = {}

    for palabra in ocurrencias.keys():
        if ocurrencias[palabra] > maximaCantidad: # si su valor es mayor a la variable..
            mayorOcurrencia = palabra # Guardo en el dicc.
            maximaCantidad = ocurrencias[palabra] # Actualizo la variable con el valor maximo hasta el momento
    print(mayorOcurrencia) # imprimo palabra con mayor ocurrencia

def desafio4Challenge(link):
    ocurrencias = {}
    texto = openText(link)
    texto = replaceCharacters(texto)
    # Convierto texto en lista
    palabras = texto.split(' ')
    ocurrencias = dictionaryOcurrences(palabras)
    biggerOcurrence(ocurrencias)

# Test
desafio4Challenge(link)
