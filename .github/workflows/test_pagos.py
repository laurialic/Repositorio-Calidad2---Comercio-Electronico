import unittest
from procesador_de_pagos import ProcesadorDePagos

class TestProcesadorDePagos(unittest.TestCase):
    def test_procesar_pago(self):
        procesador = ProcesadorDePagos()
        self.assertIn("éxito", procesador.procesar_pago(100))
        self.assertIn("Error", procesador.procesar_pago(0))

if __name__ == '__main__':
    unittest.main()
