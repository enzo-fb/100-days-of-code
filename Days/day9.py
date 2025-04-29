import random

def geraAleatorio2num(x,y):
    return random.randint(x,y)
def geraAleator():
    return random.randint(0,10000)
print(geraAleator())
x = input("Digite o primeiro número: ")
y = input("Digite o segundo número: ")
print(f"Número aleatório gerado entre {x} e {y}: ")
print(geraAleatorio2num(2,6))