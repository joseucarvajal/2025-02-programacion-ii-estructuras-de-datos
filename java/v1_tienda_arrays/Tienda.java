// Utilizar cosas que ya están hechas. Como por ejemplo los sanitarios o las ventanas o las cocinas en la construcción de una casa.
// en este caso, vamos a utilizar el objeto Scanner para leer datos de los usuarios.
import java.util.Scanner;

class Tienda {
    public static void main(String[] args) {

        //Salidas lo que se le muestra al usuario
        System.out.println("Sistema de ventas Java");

        // Entradas: Son los datos que se le piden al usuario. Usualmente, son los datos que el usuario digita por el teclado
        Scanner scanner = new Scanner(System.in);

        // Salida
        System.out.println("Ingrese el nombre del producto que va a comprar: ");
        // Entrada: Leemos el nombre del producto que va a comprar el usuario
        // Variable: nombreProducto
        String nombreProducto = scanner.nextLine(); // "Bicicleta"

        // Salida
        System.out.println("Ingrese el precio del producto: ");
        // Entrada: Leemos el precio del producto que va a comprar el usuario   
        // Variable: precioProducto
        double precioProducto = scanner.nextDouble(); // 114999.90

        // Cerramos el scanner, que es como colgar el teléfono para qeu no siga consumiendo recursos del sistema.
        scanner.close();

        // decisiones
        if (precioProducto < 0) {
            System.out.println("ERROR: El precio del producto no puede ser negativo");
        } else {
            System.out.println(String.format("Ud. ha comprado %s por un precio de %f", nombreProducto, precioProducto));
        }
    }
}