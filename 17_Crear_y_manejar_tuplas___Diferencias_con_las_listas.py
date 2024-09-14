# Se crea una tupla de colores con 10 elementos
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja')

# Se imprime el elemento en la posición 1 de la tupla 'colores'
# Las tuplas en Python son similares a las listas pero inmutables
# El índice 1 corresponde al segundo elemento, que es 'azul'
print(colores[1])

# Se crea una tupla de números
numeros = (10, 1, 5, 11)

# Se realiza una operación combinada utilizando los elementos de la tupla 'numeros'
# - numeros[2] es 5
# - numeros[1] es 1
# - numeros[0] es 10
# - numeros[-1] es 11 (el último elemento)
# La operación es: 5 - 1 + 10 + 11
operacion = numeros[2] - numeros[1] + numeros[0] + numeros[-1]

# Se imprime el resultado de la operación combinada
print(operacion)
