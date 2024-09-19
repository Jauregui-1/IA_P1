# coding: latin1

# coding: latin1 es un argumento colocado para que no de el error utf-8 producido por emplear caracteres especiales como �

# Clase que representa un producto en general
class Producto:
    # El m�todo __init__ es el constructor que inicializa los atributos del producto
    def __init__(self, nombre, categoria, precio):
        # Se asignan los atributos del producto a trav�s de 'self'
        self.nombre = nombre  # Nombre del producto (ej: Laptop, Monitor)
        self.categoria = categoria  # Categor�a del producto (ej: Computadoras, Accesorios)
        self.precio = precio  # Precio del producto en d�lares

    # M�todo para mostrar la informaci�n del producto
    def mostrar_info(self):
        # Imprime el nombre, categor�a y precio del producto
        print("Producto:",self.nombre, "Categor�a: ",self.categoria, "Precio: $",self.precio)
        
    # M�todo para cambiar el precio del producto
    def cambiar_precio(self, nuevo_precio):
        # Cambia el precio actual del producto al nuevo precio
        self.precio = nuevo_precio


# Clase vac�a que podr�a utilizarse como plantilla para futuros desarrollos
class ProductoVacio:
    # Se utiliza 'pass' ya que no hay ninguna funcionalidad dentro de esta clase
    pass


# La clase Computadora hereda de Producto, lo que significa que Computadora es un tipo de Producto
class Computadora(Producto):
    # El m�todo __init__ inicializa los atributos de Computadora, adem�s de los heredados de Producto
    def __init__(self, nombre, categoria, precio, procesador):
        # Se utiliza super() para heredar el __init__ de la clase padre (Producto)
        super().__init__(nombre, categoria, precio)
        # Se a�ade un nuevo atributo espec�fico para las computadoras: el procesador
        self.procesador = procesador

    # M�todo espec�fico para mostrar la informaci�n de una computadora
    def mostrar_info_computadora(self):
        # Imprime el nombre, categor�a, precio y procesador de la computadora
        print("Computadora:",self.nombre, "Categor�a: ",self.categoria, "Precio: $",self.precio, "Procesador: ",self.procesador)


# Variable global que representa el nombre del negocio de computadoras
nombre_global_negocio = "TechStore"

# Funci�n que gestiona el inventario del negocio
def gestion_inventario():
    # Variable local que representa el nombre del almac�n actual
    nombre_local = "Almac�n Central"
    
    # Funci�n anidada dentro de gestion_inventario, utilizada para verificar el inventario
    def verificar_inventario():
        # nonlocal permite modificar la variable 'nombre_local' desde la funci�n interna
        nonlocal nombre_local
        # Imprime el nombre del almac�n (local) y el nombre del negocio (global)
        print("Local: ",nombre_local)
        print("Negocio: ",nombre_global_negocio)
    
    # Se llama a la funci�n verificar_inventario para ejecutar el c�digo interno
    verificar_inventario()


# Pruebas de los conceptos

# Crear un objeto de la clase Producto para representar un Monitor
producto1 = Producto("Monitor LED", "Accesorios", 150)
# Mostrar la informaci�n del producto (Monitor)
producto1.mostrar_info()
# Cambiar el precio del Monitor a $180
producto1.cambiar_precio(180)
# Mostrar la informaci�n del producto con el nuevo precio
producto1.mostrar_info()


# Clase vac�a: Crear un objeto de ProductoVacio (no hace nada en este punto)
producto_vacio = ProductoVacio()


# Crear un objeto de la clase Computadora para representar una Laptop
computadora1 = Computadora("Laptop Gaming", "Computadoras", 1200, "Intel i7")
# Mostrar la informaci�n detallada de la computadora (nombre, categor�a, precio y procesador)
computadora1.mostrar_info_computadora()


# Uso de variables globales y locales
# Llamar a la funci�n para gestionar el inventario y mostrar la informaci�n del negocio
gestion_inventario()


# Eliminar objetos
# Elimina el objeto producto1 (Monitor) de la memoria
del producto1
