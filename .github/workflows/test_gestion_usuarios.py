import unittest
from gestion_de_usuarios import GestionDeUsuarios

class TestGestionDeUsuarios(unittest.TestCase):
    def test_registrar_usuario(self):
        gestion = GestionDeUsuarios()
        self.assertTrue(gestion.registrar_usuario("usuario1", "pass123"))
        self.assertFalse(gestion.registrar_usuario("usuario1", "pass456"))

if __name__ == '__main__':
    unittest.main()
