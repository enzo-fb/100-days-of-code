'''
Programa verifica se um determinado ano de entrada é um ano bissexto ou não
'''

def anoBissexto(ano):
    if ((ano%4==0 and ano%100!=0) or (ano%100==0 and ano%400==0)):
        return print(f"{ano} é um ano bissexto!")
    return print(f"{ano} não é um ano bissexto!")


ano = int (input("Digite o ano (XXXX): "))
anoBissexto(ano)