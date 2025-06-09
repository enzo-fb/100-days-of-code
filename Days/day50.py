"""Lista encadeada"""


class No:
    def __init__(self, valor):
        self.prox = None
        self.valor = valor

    def __str__(self):
        return str(self.valor)


class Lista_Encadeada:
    def __init__(self):
        self.raiz = None

    def inserir_no(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            atual = self.raiz
            while atual.prox:
                atual = atual.prox
            atual.prox = No(valor)

    def remover_no(self, valor):
        if not self.raiz:
            raise ValueError("Lista encadeada vazia!")
        if self.raiz.valor == valor:
            self.raiz = self.raiz.prox
            return
        aux = self.raiz
        anterior = None
        while aux and (aux.valor != valor):
            anterior = aux
            aux = aux.prox
        if not aux:
            raise ValueError("Valor não encontrado!")
        anterior.prox = aux.prox

    def imprimir_lista(self):
        if not self.raiz:
            raise ValueError("Lista vazia!")
        aux = self.raiz
        while aux:
            print(aux, end=" ")
            aux = aux.prox

    def verificar_lista(self):
        if not self.raiz:
            return ValueError("Lista vazia!")
        else:
            return print("Lista existente!")

    def tamanho(self):
        if not self.raiz:
            return 0
        aux = self.raiz
        contador = 0
        while aux:
            contador += 1
            aux = aux.prox
        return contador
