"""Implementar herança entre classes"""

from day40 import FormasGeometricas


class Retangulo(FormasGeometricas):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def info(self):
        return super().info()
