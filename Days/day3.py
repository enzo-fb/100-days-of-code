help(map)

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
copa = list(map(int, input("Digite os anos da Copa do Mundo que o Brasil foi campeão: ").split())) #map: serve para aplicar
                                                                                                   # uma função a cada item   
                                                                                                   # de um iterável (lista,tuplas...)
print(f"Olá, {nome}")
print(f"Você tem {idade} anos;")
print(f"Você tem {altura:.2f} de altura.")
print(f"Você digitou: {copa}")
