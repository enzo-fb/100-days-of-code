'''
    Encontre a palavra mais longa em uma string.
'''

def encontrePalavraLonga(string):
    if string == None:
        return None
    frase = str(string)
    frase = frase.lower().replace(',', ' ').split()
    palavra_longa = ['']
    for i in frase:
        if len(i) > len(palavra_longa[0]):
            palavra_longa.clear()
            palavra_longa.append(i)
        elif len(i) == len(palavra_longa[0]):
            palavra_longa.append(i)
    return palavra_longa

string = "Pato, cachorro, gato, papagaio, bananana, corredores"
print(encontrePalavraLonga(string))