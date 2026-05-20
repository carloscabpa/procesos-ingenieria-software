import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test
        self.calc = Calculadora()

    # -------- SUMA --------
    def test_sumar_positivos(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-2, -3), -5)

    def test_sumar_cero(self):
        self.assertEqual(self.calc.sumar(5, 0), 5)

    # -------- RESTA --------
    def test_restar_positivos(self):
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_restar_negativos(self):
        self.assertEqual(self.calc.restar(-5, -3), -2)

    def test_restar_cero(self):
        self.assertEqual(self.calc.restar(5, 0), 5)

    # -------- MULTIPLICACIÓN --------
    def test_multiplicar_positivos(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)

    def test_multiplicar_cero(self):
        self.assertEqual(self.calc.multiplicar(5, 0), 0)

    # -------- DIVISIÓN --------
    def test_dividir_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_negativos(self):
        self.assertEqual(self.calc.dividir(-10, 2), -5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == '__main__':
    unittest.main()