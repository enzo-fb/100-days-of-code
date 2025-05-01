"""
Este script solicita ao usuário que insira um número inteiro e 
será utilizado para verificar a paridade do número fornecido, ou seja, 
determinar se ele é par ou ímpar.
"""
def paridade(x):
    if x%2 == 0 :
        return print(f"O número {x} é par!")
    return print(f"O número {x} é ímpar!")

num = int(input("Digite um número inteiro para ser verificado: "))
paridade(num)
