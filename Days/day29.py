'''
    Dicionário de palavras e suas frequências
'''

def contagemFrequencia(frase):
    frequencia = dict()
    frase = str(frase).split()
    for palavra in frase:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    frequencia_ordenada = dict(sorted(frequencia.items(), key=lambda item: item[1], reverse=True))
    return frequencia_ordenada

frase = "o gato roeu a roupa do gato roeu"
print(contagemFrequencia(frase))