"""Hierarquia de Classes"""

import math


class FormasGeometricas:

    def area(self):
        raise NotImplementedError("Método 'area' deve ser implementado na subclasse")

    def perimetro(self):
        raise NotImplementedError(
            "Método 'perimetro' deve ser implementado na subclasse"
        )

    def info(self):
        return f"Área: {self.area()}, Perímetro: {self.perimetro()}"


class Circulo(FormasGeometricas):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def area(self):
        return math.pi * (self.raio**2)

    def perimetro(self):
        return 2 * (math.pi) * (self.raio)

    def info(self):
        return super().info()


class Quadrado(FormasGeometricas):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado**2

    def perimetro(self):
        return 4 * (self.lado)

    def info(self):
        return super().info()


class Triangulo(FormasGeometricas):
    def __init__(self, lado1, lado2, lado3, base, altura):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def info(self):
        return super().info()
