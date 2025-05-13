'''
    Função para remover duplicatas de uma lista
'''
def removerDuplicata(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado

lista = ["um", "dois", "dois", "um"]

print(lista)
lista = removerDuplicata(lista)
print(lista)