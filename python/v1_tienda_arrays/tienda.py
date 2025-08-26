# 1. Salidas
print("Sistema de ventas Python")

# Salida
print("Ingrese el nombre del producto que va a comprar: ")

# variable: nombreProducto y entrada (input)
nombreProducto = input()

# Salida
print("Ingrese el precio del producto: ")

# variable: precioProducto y entrada (input)
precioProducto = input()

# variable: precioProducto
precioProducto = float(precioProducto)

# decisiones
# variable: precioProducto
if (precioProducto < 0):
    #salida
    print("ERROR: El precio del producto no puede ser negativo")
else:
    #salida: formato
    print(f"Ud. ha comprado {nombreProducto} por un precio de {precioProducto}")