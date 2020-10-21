# Las naranjas de Miguel
# Miguel vive en un pueblo frutero con su hermana en el valle de Oz. 
# Todos los días cosecha bananas y naranjas de su campo. Como son abundantes, 
# suele darle 2 bananas y 1 naranja a su hermana. No obstante Miguel siempre 
# quiere quedarse con por lo menos una naranja, por lo cual le da una naranja 
# a su hermana solo cuando se cosechan al menos 2 naranjas.
# Miguel ahora quiere modernizarse, compró una cinta transportadora que detecta 
# cada fruta que la atraviesa y te pide ayuda para escribir un programa que reciba 
# el código generado por la máquina y devuelva la cantidad de bananas y naranjas que 
# le quedarán luego de quitar las frutas que le dará a su hermana.
# ejemploCodigoDePedido = "BBBBBNNNNNNNN"
# Cada N representa una naranja y cada B representa una banana.
# Tips
# La función list() toma un string y lo convierte a una lista

# P = list( ejemploCodigoDePedido )
# >> P = ['B', 'B', 'B', 'B', 'B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']

P = ['B', 'B', 'B', 'B', 'B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']

def naranjasDeMiguel(cadena):
    naranja = 0
    banana = 0
    for fruta in cadena:
        if (fruta=='N'):
            naranja+=1
        elif(fruta=='B'):
            banana+=1
    if(banana>1):
        banana-=2
    else:
        banana -= 1
    if(naranja>1):
        naranja-=1
    return str(banana)+" "+str(naranja)

# Test
print(naranjasDeMiguel("BB"))