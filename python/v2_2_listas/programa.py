from typing import List
from producto import Producto

lista_productos: List[Producto] = []

#función para solicitar productos
def solicitar_productos():
    solicitar_otro_producto = True
    while (solicitar_otro_producto == True):
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = input("Ingrese el precio del producto: ")
        precio_producto = float(precio_producto)
        producto = Producto(nombre_producto, precio_producto)
        lista_productos.append(producto)
        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar == "n":
            solicitar_otro_producto = False


#función para calcular el precio total de la venta
def calcular_precio_total_de_venta():
    total = 0
    for producto in lista_productos: #Acción de repetir: ciclo for, while
        total += producto.precio
    print(f"el total de la venta es {total}")


def mostrar_productos():
    for producto in lista_productos: #Acción de repetir para cada producto de la lista de productos
        print(f"el nombre del producto es {producto.nombre} y su precio es {producto.precio}")


def ordernar_productos_por_precio_descendente():
    lista_productos.sort(key=lambda producto: producto.precio, reverse=True)

def main():
    solicitar_productos() #Tarea, acción, rutina o función
    print("Productos sin ordenar:")
    mostrar_productos()
    ordernar_productos_por_precio_descendente()
    print("Productos ordenados por precio descendente:")
    mostrar_productos()
    calcular_precio_total_de_venta()

if __name__ == "__main__":
    main()