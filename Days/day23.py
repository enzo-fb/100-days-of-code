'''
    Função para encontrar a interseção de duas listas
'''

def interseccaoListas(lista1, lista2):
    lista_resultado = []
    for i in lista1:
        if i in lista2:
            lista_resultado.append(i)
    return lista_resultado


lista1 = [1,2,3,4,5]
lista2 = [1,2,5,23,44]
print(interseccaoListas(lista1,lista2))