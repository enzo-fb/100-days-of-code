"""Classe para um carro simples"""


class Carro:
    def __init__(self, nome, modelo, ano, cor):
        self.marca = nome
        self.modelo = modelo
        self.ano = ano
        self._cor = cor
        self.ligado = False

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nova_marca):
        if isinstance(nova_marca, str) and len(nova_marca) > 0:
            self._marca = nova_marca
        else:
            raise ValueError("Marca inválida! Deve ser uma string não vazia.")

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and len(novo_modelo) > 0:
            self._modelo = novo_modelo
        else:
            raise ValueError("Modelo inválido! Deve ser uma string não vazia.")

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        if (
            isinstance(novo_ano, int) and novo_ano > 1885
        ):  # O primeiro carro foi inventado em 1886
            self._ano = novo_ano
        else:
            raise ValueError("Ano inválido! Deve ser um inteiro maior que 1885.")

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        if isinstance(nova_cor, str) and len(nova_cor) > 0:
            self._cor = nova_cor
        else:
            raise ValueError("Cor inválida! Deve ser uma string não vazia.")

    @property
    def info(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Cor: {self._cor}"

    def __str__(self):
        return self.info

    @property
    def ligado(self):
        return self._ligado

    @ligado.setter
    def ligado(self, estado):
        if isinstance(estado, bool):
            self._ligado = estado
        else:
            raise ValueError("Estado deve ser um booleano (True ou False).")

    def start(self):
        self.ligado = True
        print("Carro ligado!")

    def stop(self):
        self.ligado = False
        print("Carro desligado!")
