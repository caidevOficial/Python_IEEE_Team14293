file = open("noticia.txt")
contenido = file.readlines()
caracteres = dict()
pares = []

def setOcurrences(caracteres,contenido):
    for linea in contenido:
        for caracter in linea:
            if caracter not in caracteres:
                caracteres[caracter] = 1
            else:
                caracteres[caracter] += 1
    return caracteres

def x(lista, diccionario):
    cantidadCaracteres = 0
    for caracter in caracteres:
        lista.append((caracter,caracteres[caracter]))
        cantidadCaracteres += caracteres[caracter]
    return cantidadCaracteres

def criterioOrden(s):
    palabra,ocurrencias = s
    return ocurrencias

def AnalisisIdiomas(caracteres,contenido,pares):
    cartacteres = setOcurrences(caracteres,contenido)
    cantidadCaracteres = x(pares,caracteres)
    pares = sorted(pares, key=criterioOrden, reverse=True)

    for palabra,ocurrencias in pares:
        if (palabra!=' '):
            print(palabra, "Aparece ", ocurrencias, " veces ", ocurrencias/cantidadCaracteres*100)
    

# Test //TODO arreglar
if __name__ == "__main__":
    AnalisisIdiomas(caracteres,contenido,pares)
    file.close()