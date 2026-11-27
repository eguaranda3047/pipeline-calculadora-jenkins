
import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == "__main__":
    unittest.main()
