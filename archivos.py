import os

# ruta del directorio
dir_path = "carpeta"

# obtener lista con los archivos en el directorio
files = os.listdir(dir_path)

# prefijo al file
prefijo = "nuevo_"

# iterar 
for file_name in files:
    file_path = os.path.join(dir_path,file_name)
    
    # validar si es un directorio
    if os.path.isfile(file_path):
        # obtener nuevo nombre
        new_file = prefijo+file_name

        # obtener path
        new_file_path = os.path.join(dir_path, new_file)

        # renombrar file
        os.rename(file_path,new_file_path)

