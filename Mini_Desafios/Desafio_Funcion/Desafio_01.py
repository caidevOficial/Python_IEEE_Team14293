# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan - Contraseña: 12345_
# Usuario: Pablo - Contraseña: xDcFvGbHn
# La función debe recibir como parámetros el usuario y la contraseña, 
# y debe devolver el valor True o False

# Defino las funciones
def userAndPass(user,password):
    userSetted = "Juan"
    passSetted = "12345_"
    if(user == userSetted and password == passSetted):
        return True
    else:
        return False

def checkCredentials(boolean,user):
    if(boolean):
        print(f"Access Granted, welcome back {user}!")
    else:
        print(f"You're not allowed here, {user}!")

# Chequeo datos
canAccess = userAndPass("Juan","12345_")
checkCredentials(canAccess,"Juan")
canAccess = userAndPass("Pablo","xDcFvGbHn")
checkCredentials(canAccess,"Pablo")
