'''
    Função para reverter uma lista
'''
def reverterLista2(lista):
    return lista[::-1]


def reverterLista(lista, max):
    aux = []
    for i in range(max-1,-1, -1):
        aux.append(lista[i])
    return aux

teste1 = ["coco", "banana", "pera", "maça", "uva"]

print(reverterLista(teste1,len(teste1)))
print(reverterLista2(teste1))