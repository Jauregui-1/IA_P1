# Se crea una tupla de colores con 4 elementos
colores = ('rojo', 'negro', 'blanco', 'azul')

# Se solicita al usuario que ingrese el nombre de un color
# La entrada del usuario se almacena en la variable 'pregunta'
pregunta = input('Que color buscas?: ')

# Se verifica si el color ingresado por el usuario est� en la tupla 'colores'
if pregunta in colores:
    # Si el color est� en la tupla, se imprime un mensaje indicando que el color est� incluido
    print('El color:', pregunta, 'esta incluido.')
else:
    # Si el color no est� en la tupla, se imprime un mensaje indicando que el color no est� incluido
    print('El color:', pregunta, 'no esta incluido.')
