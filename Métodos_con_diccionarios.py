# Se definen dos diccionarios: 'teclado1' y 'teclado2' con información de teclados
teclado1 = {
    'CATEGORIA': 'TECLADOS',
    'MODELO': 'HYPERX ALLOY FPS PRO',
    'PRECIO': '89.99'
}

teclado2 = {
    'CATEGORIA': 'TECLADOS',
    'MODELO': 'CORSAIR K55 RGB',
    'PRECIO': '59.99'
}

# La función len() se usa para obtener el número de claves en el diccionario 'teclado1'
x = len(teclado1)

# Se imprime el número de claves del diccionario 'teclado1'
print("El número de claves del diccionario teclado 1 es de: ", x)

# Se eliminan las claves 'CATEGORIA' y 'PRECIO' del diccionario 'teclado2'
del teclado2['CATEGORIA'], teclado2['PRECIO']

# Se imprime el diccionario 'teclado2' después de eliminar las claves
print(teclado2)
