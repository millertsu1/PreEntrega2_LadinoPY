import json

class Producto:
    productos = []

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.productos.append(self)

    @classmethod
    def ver_productos(cls):
        print("=== Productos ===")
        for producto in cls.productos:
            print("Nombre:", producto.nombre)
            print("Precio:", producto.precio)
            print("----------")

    @staticmethod
    def guardar_productos():
        productos = [p.__dict__ for p in Producto.productos]
        with open("../productos.json", "w") as file:
            json.dump(productos, file)

    @staticmethod
    def cargar_productos():
        try:
            with open("../productos.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

