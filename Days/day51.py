"""Grafo"""


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = set()

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.vertices:
            self.adicionar_vertice(vertice1)
        if vertice2 not in self.vertices:
            self.adicionar_vertice(vertice2)

        self.vertices[vertice1].add(vertice2)
        self.vertices[vertice2].add(vertice1)

    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].discard(vertice2)
            self.vertices[vertice2].discard(vertice1)

    def obter_vertices(self):
        return list(self.vertices.keys())

    def obter_arestas(self, vertice):
        return list(self.vertices[vertice])

    def __str__(self):
        return str(self.vertices)
