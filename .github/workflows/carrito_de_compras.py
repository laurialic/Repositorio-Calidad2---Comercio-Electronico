class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.verificar_disponibilidad():
            self.productos.append(producto)

    def calcular_total(self):
        return sum([p.precio for p in self.productos])
