# Armar una función que copie un archivo .xlsx, 
# y lo guarde como "Copia 1 -  nombre ", de ya 
# existir debe guardarlo como Copia 2 -, Copia 3 - , ...
# Usar la libreria os para chequear si existe el archivo:
# Tips:
# os.path.exists( nombre ) devolverá True si ya existe
# Se puede importar con: import os
import os
import shutil
from shutil import copyfile

name = "noticia.txt"
prefix = "Copia "
sufix = "1"
sign = " - "
newFileName = ""

def copyFile(sufix):
    for i in range(2,5):
        if(os.path.exists(prefix+sufix+sign+name)):
            sufix = str(i)
        else:
            newFileName = prefix+sufix+sign+name
            shutil.copyfile(name,newFileName)
            break

# Test
copyFile(sufix)