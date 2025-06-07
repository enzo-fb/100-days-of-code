"""Fila"""


class Fila:
    def __init__(self):
        self.fila = []

    def entrar(self, valor):
        self.fila.append(valor)

    def sair(self):
        if not self.fila:
            raise ValueError("Fila vazia!")
        return self.fila.pop(0)

    def esvaziar(self):
        self.fila.clear()
