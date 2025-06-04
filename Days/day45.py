"""Polimorfismo com uma calculadora"""

import math as m


class Forma:
    def calcula_area(self):
        raise NotImplementedError("Esse método tem que ser implementado na subclasse!")


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcula_area(self) -> float:
        area = float(self.lado * self.lado)
        return area


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcula_area(self):
        area = m.pi * (self.raio**2)
        return area
