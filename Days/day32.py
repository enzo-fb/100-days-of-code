'''
    Lê e exibe o conteúdo de um arquivo de texto
'''

with open("arquivo.txt", "a+") as arquivo:
    arquivo.seek(0) # volta para o inicio antes de ler
    conteudo = arquivo.read()
    print(conteudo)