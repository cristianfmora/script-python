miLista = [10, 1, 8, 3, 5]

# Adicionar un nuevo elemento
miLista.append(3)

# Adicionar un nuevo elemento en una posicion insert(ubicación,valor)
miLista.insert(2,8)

# Intercambio de variables
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1
# intercambiar listas
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

# Ordenar listas
miLista.sort()

# Revertir listas
miLista.reverse()

# copia de lstas por parte [inicio:fin], el fin no lo copa
lista = miLista[:]
lista2 = miLista[1:-2]

# validar si se encuentra información en la lista
miListas = [0, 3, 12, 8, 2]

print(5 in miListas)
print(5 not in miListas)
print(12 in miListas)
print(miLista, variable1, variable2, lista, lista2)

# ciclos y miListas
miLista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista3)):
    Encontrado = miLista3[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

# listas multidimensionales
temps = [[0.0 for h in range (24)] for d in range (31)]
print(temps)

# listas tridimensionales
habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]