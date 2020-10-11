# Realizar un programa que convierta una nota porcentual 
# del 0 al 100 a una letra entre A y F de acuerdo a la 
# siguiente conversión:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: 0–59

nota = int(input("Ingrese una nota [0-100]: "))

if(nota<60):
    nota = "F"
elif(nota>59 and nota<70):
    nota = "D"
elif(nota>69 and nota<80):
    nota = "C"
elif(nota>79 and nota<90):
    nota = "B"
elif (nota>89 and nota<101):
    nota = "A"
else:
    nota = "incorrecta: [0-100]"

print("La nota es: ")
print(nota)