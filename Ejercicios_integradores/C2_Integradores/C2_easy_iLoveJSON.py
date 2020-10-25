# La salida del programa tiene que imprimir OK si el usuario se encuentra 
# en la base de datos y si coincide la contraseña, imprimimos DNE (does not exist) 
# si el usuario no existe y NO en cualquier otro caso.

import json

data = '{"usuarios": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],"contra": ["abc123","caballitos","yoloswag"]}'

def loveJSon():
    indexMail = -1
    mensaje = "DNE"
    usuarios = json.loads(data)
    email = "mica@mail.co"
    password = "abc123"
    if(email in usuarios["usuarios"]):
        contMail = list(usuarios["usuarios"])
        contPass = list(usuarios["contra"])
        for i in contMail:
            if(email==i):
                indexMail = contMail.index(i)
                break
        if(indexMail!=-1 and password==contPass[indexMail]):
            mensaje = "OK"
    print(mensaje)

loveJSon()
