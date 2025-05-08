'''
Função para encontrar a soma de todos os elementos em uma lista.
'''

def encontrarSoma(lista):
    soma = 0
    for i in lista:
        if isinstance(i, (int, float)): #considera somente os elementos que são do tipo int e float
            soma += i
    return soma

lista = ["banana",45,"cachorro", 3, 2]
print(encontrarSoma(lista))
