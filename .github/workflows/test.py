## tests/test_carrito_de_compras.py
import unittest
from carrito_de_compras import CarritoDeCompras
from producto import Producto

class TestCarritoDeCompras(unittest.TestCase):
    def test_calculo_total(self):
        carrito = CarritoDeCompras()
        producto1 = Producto("Libro", 15.0)
        producto2 = Producto("Camisa", 25.0)
        carrito.agregar_producto(producto1)
        carrito.agregar_producto(producto2)
        self.assertEqual(carrito.calcular_total(), 40.0)

if __name__ == '__main__':
    unittest.main()
