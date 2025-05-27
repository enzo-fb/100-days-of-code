"""
Lidar com exceções para arquivo não encontrado
"""

try:
    with open("arquivo.txt", "r") as arquivo:
        for i in arquivo.readlines():
            print(i.strip())
except FileNotFoundError:
    print("Erro ao abrir o arquivo, arquivo não encontrado!")
