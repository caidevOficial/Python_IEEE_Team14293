
# Manejo de Archivos de Texto

# Se especifica el encoding para evitar problemas en windows
f = open('noticia.txt', encoding='utf-8')

# mediante estos metodos se puede modificar el separador del texto
lineas = f.readlines()
separador  = ' '.join(lineas)
print(separador)

# Usando este metodo no hace falta modificar ningun separador, ya que 
# se hace automatico.
texto = f.read()

print(texto)