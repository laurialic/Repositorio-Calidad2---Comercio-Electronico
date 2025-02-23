class Producto:
    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def verificar_disponibilidad(self):
        return self.disponible


