# Crear:
# Una función que convierta grados Celsius a grados Farenheit
# Una función que convierta grados Celsius a grados Kelvin
# El usuario debe ingresar una temperatura en grados Celsius 
# y el programa debe mostrar las conversiones a Farenheit y Kelvin 
# utilizando las funciones. Si la temperatura ingresada es inferior 
# al cero absoluto, el programa debe mostrar un mensaje de advertencia.

def temperatureConverter():

    absoluteZero = (-273.15)
    celcius = float(input("Ingrese una temperatura en °C: "))
    fahrenheite = (1.8 * celcius) +32
    kelvin = celcius + 273.15
    
    if(celcius<absoluteZero):
        print("Cuidado, la temperatura ingresada es inferior al cero absoluto!")
    else:
        print(f"[{celcius}]°C = [{fahrenheite}]°F = [{kelvin}]°K")

# Test
temperatureConverter()