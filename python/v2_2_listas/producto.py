# Clase: Una clase es un resumen de las cosas que yo necesito. 
# Una clase es una plantilla (molde - plano).
# Si yo fabrico galletas y NO tengo un molde, las galletas quedan:
# - Disparejas (unas grandes otras pequeñas)
# - Sin forma unas galletas quedan cuadradas, otras redondas.
# Si yo fabrico galletas y SI tengo un molde, las galletas quedan:
# - Con forma y todas iguales.
# - Todas quedan del mismo tamaño, del mismo peso
# - Puedo calcular cuánto me cuesta una galleta

# Con la clase Producto, puedo crear muchos objetos de productos

class Producto: # este es el molde
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio