# Definir una función que detecte si una palabra es un palíndromo y devuelve True o False.
# Ejemplos:
# palindromo( "python" ) => False
# palindromo( "reconocer" ) => True
# palindromo( "Neuquén" ) => False

def esPalindromo(cadena):
    # retorna true si es capicua
    cadena1 = cadena[::-1].lower()
    if(cadena1 == str(cadena).lower()):
        return True
    return False

x = esPalindromo("Neuquen")
print(x)