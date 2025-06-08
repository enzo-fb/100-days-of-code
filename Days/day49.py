"""Árvore Binária de Busca (ABB)"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir_no(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)
        return no

    def remover_no(self, valor, no=None):
        if no is None:
            no = self.raiz
        if no is None:
            raise ValueError("Sem valores para serem removidos")
        if valor < no.valor:
            no.esquerda = self.remover_no(valor, no.esquerda)
        elif valor > no.valor:
            no.direita = self.remover_no(valor, no.direita)
        else:
            # Nó encontrado
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._min_value_node(no.direita)
            no.valor = temp.valor
            no.direita = self.remover_no(temp.valor, no.direita)
        if no == self.raiz:
            self.raiz = no
        return no

    def _min_value_node(self, node):
        current = node
        while current.esquerda is not None:
            current = current.esquerda
        return current

    def buscar_no(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar(no.esquerda, valor)
        return self._buscar(no.direita, valor)
