# Se crea una lista de colores con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se utiliza el método pop() para eliminar y obtener elementos de la lista:
# - colores.pop(1) elimina y devuelve el elemento en la posición 1, que es 'azul'
# - colores.pop(-2) elimina y devuelve el elemento en la posición -2 (el penúltimo), que es 'blanco'
# Los elementos eliminados se almacenan en la tupla 'nueva_lista'
nueva_lista = colores.pop(1), colores.pop(-2)

# Se imprime la tupla 'nueva_lista' con los elementos eliminados
print(nueva_lista, '\n')

# Se imprime la lista 'colores' después de las eliminaciones
print(colores)
