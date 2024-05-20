d = {
    'Nombre':'Cristian',
    'Apellido':'Mora',
    'edad':'30',
    'ciudad':'Bogotá'
}
""" Recorrer clave y valor al mismo tiempo """
for key,value in d.items():
    print(key,":", value)

""" Recorrer solo el valor """
for valor in d.values():
  print(valor)

""" Recorrer claves """
for clave in d.keys():
  print(clave)
