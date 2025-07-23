def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando função: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Função {func.__name__} terminou")
        return resultado

    return wrapper


@meu_decorador
def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Enzo")


class MeuDescritor:
    def __init__(self, valor_inicial=None):
        self.valor = valor_inicial

    def __get__(self, instance, owner):
        print("Obtendo valor do descritor")
        return self.valor

    def __set__(self, instance, value):
        print(f"Definindo valor do descritor para {value}")
        self.valor = value


class MinhaClasse:
    atributo = MeuDescritor(10)


obj = MinhaClasse()
print(obj.atributo)
obj.atributo = 42
print(obj.atributo)
