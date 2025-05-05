'''
Calcula o fatorial de um número
'''

def calculaFatorial(num):
    fat = aux = 1
    while aux<=num:
        fat = fat*aux
        aux+=1
    return fat
        
num = int(input("Digite um número inteiro para calcular o fatorial: ")) 
print(calculaFatorial(num))