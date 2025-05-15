'''
    Função para contar a frequência de palavras em uma frase.
'''

def contarFrequencia(frase):
    lista = frase.split()
    contagem = {}
    for i in lista:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    return print( contagem)


string = "cachorro gato gato cachorro gato gato"
contarFrequencia(string)