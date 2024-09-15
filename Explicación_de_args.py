# Se define una funci�n llamada 'colores' que toma un n�mero arbitrario de argumentos utilizando *args
def colores(*args):
    # Se accede a los elementos de 'args' por su �ndice, y se imprime un mensaje con los colores
    print('El color', args[2], 'es mi favorito. Pero el color', args[0], 'tampoco esta mal.')

# Se llama a la funci�n 'colores' con varios colores como argumentos
colores('negro', 'azul', 'rojo', 'morado')

# Se define una funci�n llamada 'suma' que tambi�n toma un n�mero arbitrario de argumentos utilizando *args
def suma(*args):
    # Se accede a los elementos por su �ndice, y se suman los valores en los �ndices 3, 6, 1, 5 y el �ltimo (-1)
    resultado = args[3] + args[6] + args[1] + args[5] + args[-1]
    # Se imprime el resultado de la suma
    print(resultado)

# Se llama a la funci�n 'suma' con una serie de n�meros del 0 al 10 como argumentos
suma(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



