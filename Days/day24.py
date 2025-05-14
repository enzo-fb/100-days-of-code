'''
    Função para converter uma lista de palavras em uma frase
'''

def palavrasFrase(lista):
    new_lista = " ".join(str(x) for x in lista) # converte todos os membros da lista para string antes de juntar
    return print(new_lista)

lista = ["ovo","galinha", "pato"]
palavrasFrase(lista)