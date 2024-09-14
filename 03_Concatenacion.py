# Definimos varias variables de tipo texto (string).
palabra01 = 'Hola'          # Guarda el texto "Hola"
palabra02 = 'mundo.'        # Guarda el texto "mundo."
palabra03 = 'Adios.'        # Guarda el texto "Adios."
Nombre = 'Jared'            # Guarda el nombre "Jared"
ApellidoP = 'Rodriguez'     # Guarda el apellido paterno "Rodriguez"
ApellidoM = 'Jauregui'      # Guarda el apellido materno "Jauregui"
num01 = '10'                # Guarda el número "10" como texto (string)
num02 = '22'                # Guarda el número "22" como texto (string)

# Concatenamos 'palabra01' y 'palabra02' en una nueva variable llamada 'palabra_completa01'.
# Esto une las dos palabras sin espacio entre ellas.
palabra_completa01 = palabra01 + palabra02
print(palabra_completa01)    # Imprime "Holamundo." (sin espacio entre "Hola" y "mundo.")

# Concatenamos 'palabra01' y 'palabra02', pero ahora agregamos un espacio entre ellas.
palabra_completa02 = palabra01 + ' ' + palabra02
print(palabra_completa02)    # Imprime "Hola mundo." (con espacio entre "Hola" y "mundo.")

# Concatenamos 'palabra_completa02' con 'palabra03', con un espacio entre ellas.
palabra_completa03 = palabra_completa02 + ' ' + palabra03
print(palabra_completa03)    # Imprime "Hola mundo. Adios."

# Concatenamos el nombre completo uniendo 'Nombre', 'ApellidoP' y 'ApellidoM' con espacios entre ellos.
nombre_completo = Nombre + ' ' + ApellidoP + ' ' + ApellidoM
print(nombre_completo)       # Imprime "Jared Rodriguez Jauregui"

# Concatenamos 'num01' y 'num02', pero como son cadenas de texto, se unirán como si fueran palabras.
numero_completo = num01 + num02
print(numero_completo)       # Imprime "1022" (se concatenan los números como texto, no como números)
