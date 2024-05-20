from math  import *

def create(lista1,lista2):
    return lista1,lista2

lista = {'nombre': 'luis','edad':25, 'Nacionalidad':'Colombia','Profesion':'Enfermero','Genero':'Masculino'}
lista3 = [1,2,3,4]

#print(create(lista,lista3))

lista = {'nombre': 'luis','edad':25, 'Nacionalidad':'Colombia','Profesion':'Enfermero','Genero':'Masculino'}

for indice, palabra in enumerate(lista):
    print("pregunta", indice+1, 'es', palabra)

for pregunta, respuesta in lista.items():
    print(pregunta,':', respuesta)

def Funcion(a,b,c):
    """Formula general
    a una ecuación"""
    raiz = b**2 - 4*a*c
    division = (2*a)
    if raiz > 0 and division > 0:
        x1 = (-b + sqrt(raiz))/division
        x2 = (-b - sqrt(raiz))/division
        print(x1,x2)
    else:
        print('error en la operación')
Funcion(1,-5,6)