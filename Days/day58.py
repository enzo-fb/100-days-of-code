"""Algoritmo de busca em profundidade (DFS)"""


def busca_profundidade(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=" ")
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_profundidade(grafo, vizinho, visitados)


# Exemplo de uso
grafo = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
busca_profundidade(grafo, "A")
