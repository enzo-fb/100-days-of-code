"""Algoritmos de Busca"""


def busca_binaria(lista, valor):
    if not lista:
        return None
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return None


def busca_linear(lista, valor):
    if not lista:
        return None
    for i, item in enumerate(lista):
        if item == valor:
            return i
    return None
