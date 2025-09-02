from producto import Producto

def main():
    #producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9, producto10: son objetos de la clase Producto
    # Tengo 10 objetos y una sola clase que es la clase Producto
    producto1 = Producto("Galletas", 1000)
    producto2 = Producto("Coca Cola", 2000)
    producto3 = Producto("Papas", 3000)
    producto4 = Producto("Agua", 4000)
    producto5 = Producto("Cerveza", 5000)
    producto6 = Producto("Coca Cola", 6000)
    producto7 = Producto("Papas", 7000)
    producto8 = Producto("Agua", 8000)
    producto9 = Producto("Cerveza", 9000)
    producto10 = Producto("Coca Cola", 10000)   


    print(f"el nombre del producto5 es {producto5.nombre} y su precio es {producto5.precio}")

if __name__ == "__main__":
    main()