num = int(input("Digite um número inteiro: "))

if num%2 == 0:
    print("Número é par!")
else:
    print("Número é ímpar!")
    
idade = int(input("Digite a sua idade: "))

if idade<12:
    print("Você é uma criança!")
elif idade>11 and idade<17:
    print("Você é um adolescente!")
elif idade>16 and idade<60:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1>num2:
    if num1>num3:
        print(f"Este é o maior número entre os três: {num1}")
elif num2>num1:
    if num2>num3:
        print(f"Este é o maior número entre os três: {num2}")
if num3>num1 and num3>num2: 
        print(f"Este é o maior número entre os três: {num3}")


num_entrada = int(input("Digite um número: "))
sum = 0
for i in range(1,num_entrada+1):
    sum += i 
print(f"A soma dos números até {num_entrada} é {sum}")


n = int(input("Digite o número para calcular seu fatorial: "))
fat = 1
while n!=1:
    fat*= n
    n -= 1
print(fat)