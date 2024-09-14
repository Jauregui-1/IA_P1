# Se crea una lista de colores con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se eliminan elementos espec�ficos de la lista usando el m�todo remove()
# - El m�todo remove('amarillo') elimina la primera aparici�n del elemento 'amarillo'
# - El m�todo remove('rojo') elimina la primera aparici�n del elemento 'rojo'
colores.remove('amarillo'), colores.remove('rojo')

# Se imprime la lista modificada, mostrando los elementos restantes despu�s de las eliminaciones
print(colores)
