"""Aplicação CRUD"""


class Crud:
    def __init__(self):
        self.sistema = None

    def criar(self):
        if self.sistema is None:
            self.sistema = set()
        else:
            raise SystemError("Sistema já criado")

    def ler(self, valor):
        if not self.sistema:
            raise KeyError("Sem elementos no sistema")
        if valor in self.sistema:
            return valor
        raise ValueError("Parâmetro não encontrado!")

    def atualizar(self, valor_pra_atualizar, novo_valor):
        if not self.sistema:
            raise KeyError("Sem elementos no sistema")
        if valor_pra_atualizar in self.sistema:
            self.sistema.remove(valor_pra_atualizar)
            self.sistema.add(novo_valor)
            return "Valor Atualizado"
        raise ValueError("Parâmetro não encontrado!")

    def excluir(self, valor):
        if not self.sistema:
            raise KeyError("Sem elementos no sistema")
        if valor in self.sistema:
            self.sistema.remove(valor)
            return
        raise ValueError("Parâmetro não encontrado!")
