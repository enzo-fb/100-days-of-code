"""Algoritmo de busca em largura (BFS)"""

from collections import deque


def busca_largura(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    visitados.add(inicio)

    while fila:
        vertice = fila.popleft()
        print(vertice, end=" ")

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
