'''
    Calcular a média de números em um arquivo de texto
'''

def calcularNumeros(Nomearquivo):
    soma = 0
    contador = 0
    with open(Nomearquivo, 'r') as arquivo:
        for linha in arquivo:
            try:
                numero = int(linha.strip())
                soma += numero
                contador += 1
            except ValueError:
                continue
    return soma / contador if contador > 0 else 0

print(calcularNumeros("arquivo.txt"))