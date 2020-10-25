# Challenge: Modificar la función para ignorar espacios, signos de puntuación, 
# y que no haga distinción entre mayúsculas y minúsculas (pueden usar str.lower). 
# Sugerimos usar el nombre del desafío como un palindromo de ejemplo.
import re,string

def esPalindromoMedium(cadena):
    cadena = re.sub('[%s]' % re.escape(string.punctuation), '', cadena).lower() #saco signos de puntuacion y normalizo minuscula
    cadena = cadena.replace(" ","") # saco espacios
    cadena1 = cadena[::-1] # copio cadena invertida
    if(cadena1 == str(cadena)):
        return True
    return False

x = esPalindromoMedium("Acaso hubo buhos aca.")
print(x)