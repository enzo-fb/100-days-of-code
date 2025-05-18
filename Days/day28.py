'''
    Inverta as palavras em uma frase, ou seja, as letras e a ordem
'''

def invertaFrase(frase):
    if frase == None:
        return None
    frase = str(frase).lower().split()
    for i in frase[::-1]:
        print(i[::-1], end=' ') 
    

invertaFrase("hello world")