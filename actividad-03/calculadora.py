class Calculadora:
    """Calculadora básica con las cuatro operaciones matemáticas principales."""

    def sumar(self, a, b):
        """Devuelve la suma de dos números."""
        return a + b

    def restar(self, a, b):
        """Devuelve la resta de dos números."""
        return a - b

    def multiplicar(self, a, b):
        """Devuelve el producto de dos números."""
        return a * b

    def dividir(self, a, b):
        """
        Devuelve el cociente de dos números.

        Lanza un ValueError si se intenta dividir entre cero.
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero")

        return a / b