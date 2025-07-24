"""Metaclasses"""


class MinhaMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Criando a classe: {name}")
        namespace["criado_por_metaclasse"] = True
        return super().__new__(mcs, name, bases, namespace)


class MinhaClasse(metaclass=MinhaMeta):
    pass


print(MinhaClasse.criado_por_metaclasse)
