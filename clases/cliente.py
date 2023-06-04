import json

class Cliente:
    def __init__(self, nombre, direccion, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def imprimir_informacion(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.telefono)
        print("Correo: ", self.correo)

    def solicitar_inicio_sesion(self):
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        # Lógica para iniciar sesión
        print("Iniciando sesión...")

    def guardar_cliente(self):
        clientes = self.cargar_clientes()
        for cliente in clientes:
            if cliente['nombre'] == self.nombre:
                print("El cliente ya existe.")
                return
            else:
                print("El cliente se creo correctamente")
        clientes.append(self.__dict__)
        with open("../clientes.json", "w") as file:
            json.dump(clientes, file)


    @staticmethod
    def cargar_clientes():
        try:
            with open("../clientes.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def mostrar_clientes():
        clientes = Cliente.cargar_clientes()
        if clientes:
            print("=== Clientes ===")
            for cliente in clientes:
                c = Cliente(cliente['nombre'], cliente['direccion'], cliente['telefono'], cliente['correo'])
                c.imprimir_informacion()
                print("----------")
        else:
            print("No hay clientes registrados.")

