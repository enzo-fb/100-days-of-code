'''
    Acrescentar dados a um arquivo de texto existente.
'''

with open("arquivo.txt", "a+") as arquivo:
    arquivo.seek(0)
    if arquivo.read() == "":
        arquivo.write("New data")    
    else:
        arquivo.write("\nNew data")
     