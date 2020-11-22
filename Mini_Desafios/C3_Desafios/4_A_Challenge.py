# Encontrar la palabra con mayor numero de ocurrencias 
# en el texto de la noticia.
link = 'noticia.txt'

def openText(link):
    f = open(link, encoding='utf-8')
    texto = f.read()
    return texto

def replaceCharacters(texto):
    reemplazar = ['’s','—',',','.','\n','\ufeff']
    for indeseado in reemplazar:
        texto = texto.replace(indeseado,' ')
    return texto

def dictionaryOcurrences(palabras):
    # Hago diccionario para contar ocurrencias
    ocurrencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra != '' and (palabra=='trump' or palabra=='the'):
            if palabra not in ocurrencias:
                ocurrencias[palabra] = 1
            else:
                ocurrencias[palabra] += 1
    return ocurrencias

def biggerOcurrence(ocurrencias):
    maximaCantidad = 0
    mayorOcurrencia = {}

    for palabra in ocurrencias.keys():
        if ocurrencias[palabra] > maximaCantidad:
            mayorOcurrencia = palabra
            maximaCantidad = ocurrencias[palabra]
    print(mayorOcurrencia)

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
