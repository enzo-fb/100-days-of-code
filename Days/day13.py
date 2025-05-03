'''
O programa encontra o maior entre três números
'''
def maiorNumero(num1,num2 = 0,num3 = 0):
    if num1==num2 == num3:
        return num1
    if num1>num2:
        if num1>num3:
            return num1
    if num2>num1:
        if num2>num3:
            return num2
    return num3


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
print(maiorNumero(num1,num2,num3))