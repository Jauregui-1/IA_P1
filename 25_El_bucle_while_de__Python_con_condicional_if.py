# Se inicializa la variable x con valor 0
x = 0

# Se inicia un bucle while que se ejecuta mientras x sea menor o igual a 30
while x <= 30:
    # Se imprime el valor actual de x
    print('El valor del bucle es: ', x)
    # Se incrementa x en 1 en cada iteración del bucle
    x += 1
    
    # Se verifica si x es igual a 4, 6 o 10
    if x == 4 or x == 6 or x == 10:
        # Si x es igual a uno de estos valores, se imprime un mensaje indicando que se saltó el valor
        print('Se salto el valor: ', x, 'de X')
        # La instrucción continue omite el resto del código en el bucle y pasa a la siguiente iteración
        continue
    
    # Se verifica si x es igual a 15
    if x == 15:
        # Si x es igual a 15, se imprime un mensaje indicando que el bucle se rompió
        print('Se rompio el bucle estando en: ', x, 'de X')
        # La instrucción break rompe el bucle, saliendo de él inmediatamente
        break
