'''
Função para contar o número de vogais em uma string.
'''
vogais = ("a", "e", "i", "o", "u")
def contaVogais(palavra):
    contador = 0
    for i in palavra:
        if i in vogais:
            contador += 1
    return contador

x = str(input("Digite uma palavra pra contar suas vogais: "))
print(contaVogais(x))