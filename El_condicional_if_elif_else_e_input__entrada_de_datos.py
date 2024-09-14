# Solicita al usuario que ingrese su edad y convierte la entrada a un entero
edad = int(input('Cual es tu edad?: '))

# Se eval�a la edad ingresada con una serie de condiciones para determinar la categor�a de edad
if edad <= 0:
    # Si la edad es menor o igual a 0, se considera un valor no v�lido
    print('Esa edad no existe.')
elif edad > 0 and edad <= 18:
    # Si la edad est� entre 1 y 18 a�os, se considera menor de edad
    print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
    # Si la edad est� entre 19 y 45 a�os, se considera un adulto joven
    print('Eres un adulto joven.')
elif edad > 45 and edad <= 100:
    # Si la edad est� entre 46 y 100 a�os, se considera un adulto mayor
    print('Eres un adulto mayor.')
elif edad > 100 and edad <= 120:
    # Si la edad est� entre 101 y 120 a�os, se considera una leyenda
    print('Eres una leyenda.')
else:
    # Si la edad es mayor a 120, se considera un dato no v�lido
    print('Dato no valido.')
