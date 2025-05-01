import random

def gera_aleatorio_entre_dois_numeros(x, y):
    """Gera um número aleatório entre x e y (inclusive)."""
    return random.randint(x, y)

def gera_aleatorio():
    """Gera um número aleatório entre 0 e 10.000."""
    return random.randint(0, 10000)

# Exibe um número aleatório entre 0 e 10.000
print(f"Número aleatório gerado entre 0 e 10.000: {gera_aleatorio()}")

# Solicita ao usuário dois números
try:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(f"Número aleatório gerado entre {x} e {y}: {gera_aleatorio_entre_dois_numeros(x, y)}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")