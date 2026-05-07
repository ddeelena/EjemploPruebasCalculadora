import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.sumar(5, 5), 10)

    def test_resta(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)

    def test_division_exitosa(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_division_por_cero(self):
        """Verifica que se lance una excepción controlada"""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()