# Se crea una lista de colores con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se eliminan elementos espec�ficos de la lista usando el �ndice:
# - El �ndice 1 corresponde al elemento 'azul'
# - El �ndice 4 corresponde al elemento 'marron'
# - El �ndice -4 corresponde al cuarto elemento desde el final, que es 'rosa'
# - El �ndice -3 corresponde al tercer elemento desde el final, que es 'blanco'
# Usamos la instrucci�n 'del' para eliminar estos elementos de la lista
del colores[1], colores[4], colores[-4], colores[-3]

# Se imprime la lista modificada, mostrando los elementos restantes despu�s de las eliminaciones
print(colores)
