# Encontrar la cantidad de ocurrencias de la palabras 
# "Trump" y "the" en el texto de la noticia.

nametext = 'noticia.txt'

def openText(nameText):
    f = open(nameText, encoding='utf-8')
    texto = f.read()
    return texto

def replaceCharacters(texto):
    reemplazar = ['’s','—',',','.','\n','\ufeff']
    for indeseado in reemplazar:
        texto = texto.replace(indeseado,' ')
    return texto

def dictionaryOcurrences(palabras):
    ocurrencias = {} # Hago diccionario para contar ocurrencias
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra != '' and (palabra=='trump' or palabra=='the'):
            if palabra not in ocurrencias:
                ocurrencias[palabra] = 1
            else:
                ocurrencias[palabra] += 1
    print(ocurrencias)

def desafio4A(nametext):
    texto = openText(nametext)
    texto = replaceCharacters(texto)
    # Convierto texto en lista
    palabras = texto.split(' ')
    dictionaryOcurrences(palabras)

# Test
desafio4A(nametext)
