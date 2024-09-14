# Solicita al usuario que ingrese su edad y convierte la entrada a un entero
edad = int(input('Cual es tu edad?: '))

# Se evalúa la edad ingresada con una serie de condiciones para determinar la categoría de edad
if edad <= 0:
    # Si la edad es menor o igual a 0, se considera un valor no válido
    print('Esa edad no existe.')
elif edad > 0 and edad <= 18:
    # Si la edad está entre 1 y 18 años, se considera menor de edad
    print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
    # Si la edad está entre 19 y 45 años, se considera un adulto joven
    print('Eres un adulto joven.')
elif edad > 45 and edad <= 100:
    # Si la edad está entre 46 y 100 años, se considera un adulto mayor
    print('Eres un adulto mayor.')
elif edad > 100 and edad <= 120:
    # Si la edad está entre 101 y 120 años, se considera una leyenda
    print('Eres una leyenda.')
else:
    # Si la edad es mayor a 120, se considera un dato no válido
    print('Dato no valido.')
