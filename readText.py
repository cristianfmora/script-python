"""
Crear un json a partir de un archivo de texto
con separación :
"""

variables = {} 
with open("archivo.txt", "r") as datos:
    for linea in datos:
        nombre, valor = linea.strip().split(":", maxsplit=1)
        variables[nombre] = valor 
    print(variables)


print (variables.values())