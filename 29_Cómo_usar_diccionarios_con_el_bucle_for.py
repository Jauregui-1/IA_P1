# Se crea un diccionario llamado 'teclado1' con información sobre un teclado
teclado1 = {
    'CATEGORIA': 'TECLADOS',
    'MODELO': 'HYPERX ALLOY FPS PRO',
    'PRECIO': '89.99'
}

# Se crea un segundo diccionario llamado 'teclado2' con información sobre otro teclado
teclado2 = {
    'CATEGORIA': 'TECLADOS',
    'MODELO': 'CORSAIR K55 RGB',
    'PRECIO': '59.99'
}

# Se itera sobre cada clave en el diccionario 'teclado1'
# En cada iteración, se imprime la clave y su valor correspondiente en el diccionario
for x in teclado1:
    print(x, '=', teclado1[x], '.')

# Se imprime una línea en blanco para separar la salida de los dos bucles
print('\n')

# Se actualiza el precio del teclado en el diccionario 'teclado2' a '30.00'
teclado2['PRECIO'] = '30.00'

# Se itera sobre cada clave en el diccionario 'teclado2'
# En cada iteración, se imprime la clave y su valor correspondiente en el diccionario
for y in teclado2:
    print(y, '=', teclado2[y], '.')
