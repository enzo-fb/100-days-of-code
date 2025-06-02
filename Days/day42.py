"""Classe para uma conta bancária com métodos de depósito e retirada"""


class ContaBancaria:
    def __init__(self, titular, agencia, tipo_conta):
        self._saldo = 0
        self.titular = titular
        self.agencia = agencia
        self.tipo_conta = tipo_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo = self.saldo + valor

    def retirada(self, valor):
        if valor <= 0:
            raise ValueError("O valor da retirada deve ser positivo.")
        if self.saldo - valor < 0:
            raise ValueError("Saldo insuficiente.")
        self.saldo = self.saldo - valor
