"""Tabela de Hash"""

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
    
    def _hash(self, chave):
        if isinstance(chave, str):
            return sum(ord(c) for c in chave) % self.tamanho
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

