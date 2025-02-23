import unittest
from producto import Producto
from carrito_de_compras import CarritoDeCompras

class TestCarritoDeCompras(unittest.TestCase):
    def test_agregar_y_calcular_total(self):
        producto = Producto("Camisa", 20, 10)
        carrito = CarritoDeCompras()
        carrito.agregar_producto(producto, 2)
        self.assertEqual(carrito.calcular_total(), 40)

if __name__ == '__main__':
    unittest.main()
