from clases.cliente import Cliente
from clases.producto import Producto

clientes = []
productos = []

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    cliente = Cliente(nombre, direccion, telefono, correo)
    cliente.guardar_cliente()
    clientes.append(cliente)


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(nombre, precio)
    producto.guardar_productos()
    productos.append(producto)
    print("Producto agregado con éxito.")

def realizar_compra():
    nombre_cliente = input("Ingrese el nombre del cliente que realiza la compra: ")
    cliente = None
    for c in clientes:
        if c.nombre == nombre_cliente:
            cliente = c
            break
    if not cliente:
        print("Cliente no encontrado.")
        return

    nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
    producto = None
    for p in productos:
        if p.nombre == nombre_producto:
            producto = p
            break
    if not producto:
        print("Producto no encontrado.")
        return

    print("Cliente:", cliente.nombre)
    print("Producto:", producto.nombre)
    print("Precio:", producto.precio)
    print("¡Compra realizada con éxito!")

def mostrar_menu():
    print("=== Menú Tienda Comunal===")
    print("1. Agregar cliente")
    print("2. Agregar producto")
    print("3. Realizar compra")
    print("4. Ver productos")
    print("5. Ver clientes")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        realizar_compra()
    elif opcion == "4":
        Producto.ver_productos()  # Método para ver los productos agregados
    elif opcion == "5":
        Cliente.mostrar_clientes()  # Método para ver los clientes agregados
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
