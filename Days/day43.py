"""implementar encapsulamento"""


class Quadrado:
    def __init__(self, lado, area, perimetro):
        self.lado = lado  # público
        self._area = area  # protegido
        self.__perimetro = perimetro  # privado

    @property
    def lado(self):
        return self.lado

    @lado.setter
    def lado(self, novo_lado):
        self.lado = novo_lado

    @property
    def perimetro(self):
        return self.__perimetro

    @perimetro.setter
    def perimetro(self, novo_perimetro):
        if (4 * self.lado) == novo_perimetro:
            self.__perimetro = novo_perimetro
        else:
            raise ValueError("Valor não condizente com o perímetro real do quadrado")
