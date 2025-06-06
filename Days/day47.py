"""implementar pilha"""


class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if not self.pilha:
            raise ValueError("Pilha vazia!")
        return self.pilha.pop()

    def mostrar_pilha(self):
        return self.pilha

    def zerar_pilha(self):
        self.pilha.clear()
