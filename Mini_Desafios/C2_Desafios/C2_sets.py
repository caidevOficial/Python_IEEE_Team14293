#Se cuentan con varios sets que contienen las personas que les gusta un cierto sabor de helado:
# vainilla = { "Juan", "Marina", "Tomas", "Paula" }
# chocolate = { "Pedro", "Paula", "Marina" }
# dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }
# Responder usando operaciones de sets:
# 1 - Hay alguna persona que le gusten todos los gustos?
# 2 - Hay alguna persona que le gusten la vainilla y no el dulce de leche?
# 3 - Cuantas personas distintas tenemos?

vainilla = { "Juan", "Marina", "Tomas", "Paula" }
chocolate = { "Pedro", "Paula", "Marina" }
dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

# Ejercicio 1
def saberTodosLosGustos():
    todosGustos = vainilla & chocolate & dulceDeLeche
    print("Le gusta todos los sabores a:")
    print(todosGustos)

# Ejercicio 2
def saberVainillaNoDDL():
    saberPersona = vainilla-dulceDeLeche
    print("Le gusta vainilla pero no DDL a:")
    print(saberPersona)

# Ejercicio 3
def personasDistintas():
    distintas = vainilla | chocolate | dulceDeLeche
    print("Personas distintas: ")
    print(distintas)

# Test
# Ejercicio 1
saberTodosLosGustos()
print("-----------------")
# Ejercicio 2
saberVainillaNoDDL()
print("-----------------")
# Ejercicio 3
personasDistintas()