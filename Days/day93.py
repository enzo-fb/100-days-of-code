"""Otimização de Código"""

import cProfile


def funcao_lenta():
    total = 0
    for i in range(1000000):
        total += i
    return total


# Comparação de duas implementações de soma de lista
# Versão lenta
def soma_lista(lista):
    total = 0
    for item in lista:
        total += item
    return total


# Versão rápida
def soma_lista(lista):
    return sum(lista)


cProfile.run("funcao_lenta()")
