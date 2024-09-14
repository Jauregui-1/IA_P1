# Se crea una lista de colores con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se convierte la lista 'colores' en una tupla y se asigna a la variable 'COLORES'
# El constructor tuple() toma una lista como argumento y crea una tupla con los mismos elementos
COLORES = tuple(colores)

# Se imprime la tupla 'COLORES' y el tipo de dato de 'COLORES'
# La función type() devuelve el tipo de dato del objeto pasado como argumento
print(COLORES, '\n', 'Tipo de dato: ', type(COLORES))
