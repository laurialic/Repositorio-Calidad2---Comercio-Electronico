import unittest
from producto import Producto

class TestProducto(unittest.TestCase):
    def test_actualizar_stock(self):
        producto = Producto("Camisa", 20, 10)
        self.assertTrue(producto.actualizar_stock(5))
        self.assertEqual(producto.stock, 5)
        self.assertFalse(producto.actualizar_stock(10))

if __name__ == '__main__':
    unittest.main()
