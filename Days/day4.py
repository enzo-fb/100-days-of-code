num1 = int (input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))


print(f"Adição: {(num1+num2)}")
print(f"Subtração: {num1-num2}")
print(f"Multiplicação: {num1*num2}")
print(f"Divisão: {num1/num2}")
print(f"Divisão (parte inteira): {num1//num2}")
print(f"Resto: {num1&num2}")
print(f"Exponenciação: {num1**num2}")

print("Comparações entre os números:")
print(f"Os números são iguais? {num1 == num2}")
print(f"Os números são diferentes? {num1 != num2}")
print(f"O primeiro número é maior que o segundo? {num1 > num2}")
print(f"O primeiro número é menor que o segundo? {num1 < num2}")
print(f"O primeiro número é maior ou igual ao segundo? {num1 >= num2}")
print(f"O primeiro número é menor ou igual ao segundo? {num1 <= num2}")

valor_true = True
valor_false = False

print(f"Valor True AND Valor False: {valor_true and valor_false}")
print(f"Valor True OR Valor False: {valor_true or valor_false}")
print(f"NOT Valor True: {not valor_true}")
print(f"NOT Valor False: {not valor_false}")
