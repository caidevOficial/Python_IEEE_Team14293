# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan - Contraseña: 12345_
# Usuario: Pablo - Contraseña: xDcFvGbHn
# La función debe recibir como parámetros el usuario y la contraseña, 
# y debe devolver el valor True o False

# Defino las funciones
def userAndPass(user,password):
    success = False
    if((user == "Juan" and password == "12345_") or (user=="Pablo" and password=="xDcFvGbHn")):
        success = True
    return success

def checkCredentials(boolean,user):
    if(boolean):
        print(f"Access Granted, welcome back {user}!")
    else:
        print(f"You're not allowed here, {user}!")

# Chequeo datos
# Caso de Suceso
canAccess = userAndPass("Juan","12345_")
checkCredentials(canAccess,"Juan")
canAccess = userAndPass("Pablo","xDcFvGbHn")
checkCredentials(canAccess,"Pablo")
# Caso de Error
canAccess = userAndPass("Admin","root")
checkCredentials(canAccess,"Admin")
