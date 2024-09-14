# Se crea una lista de colores con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se eliminan elementos específicos de la lista usando el método remove()
# - El método remove('amarillo') elimina la primera aparición del elemento 'amarillo'
# - El método remove('rojo') elimina la primera aparición del elemento 'rojo'
colores.remove('amarillo'), colores.remove('rojo')

# Se imprime la lista modificada, mostrando los elementos restantes después de las eliminaciones
print(colores)
