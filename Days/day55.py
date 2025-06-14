"""Classe iterável"""


class Intera:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        self.atual = 0
        return self

    def __next__(self):
        if self.atual < self.limite:
            x = self.atual
            self.atual += 1
            return x
        else:
            raise StopIteration
