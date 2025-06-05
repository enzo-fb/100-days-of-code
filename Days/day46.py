"""Decoradores de classes"""


def adiciona_repr(cls):
    def __repr__(self):
        return f"{cls.__name__}(atributos={self.__dict__})"

    cls.__repr__ = __repr__

    def __init__(self, name, age):
        if not isinstance(name, str):
            raise ValueError("Este nome deve ser uma string")
        if not isinstance(age, int):
            raise ValueError("Esta idade deve ser um inteiro")
        self.name = name
        self.age = age

    cls.__init__ = __init__

    return cls


@adiciona_repr
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
