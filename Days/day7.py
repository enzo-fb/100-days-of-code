# Lista inicial de frutas
frutas = ['laranja', 'pera', 'banana', 'maça', 'tomate']

# Função para imprimir a lista de frutas
def printar_frutas(lista):
    print(lista)

# Imprime a lista inicial de frutas
printar_frutas(frutas)

# Adiciona uma fruta fornecida pelo usuário
fruta_usuario = input("Digite uma fruta: ").strip()
frutas.append(fruta_usuario)

# Imprime a lista após adicionar a fruta do usuário
printar_frutas(frutas)

# Modifica a lista: remove 'maça' e insere 'pera' no início
if 'maça' in frutas:
    frutas.remove('maça')
frutas.insert(0, 'pera')

# Imprime a lista final
printar_frutas(frutas)

# Função para dividir a lista em fatias de tamanho especificado
def dividir_lista(lista, tamanho):
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

# Divide a lista em fatias de tamanho 2 e imprime
printar_frutas(dividir_lista(frutas, 2))

############ TUPLAS #################

# Define uma tupla com diferentes tipos de elementos
coisas = ('carro', 23, True, 1.87, ' rapido')

# Imprime o quarto elemento da tupla
print(coisas[3])

# Concatena o primeiro elemento com o quinto elemento repetido duas vezes
print(coisas[0] + coisas[4] * 2)

# Verifica se 'carro' está na tupla
print('carro' in coisas)

# Converte a tupla em uma lista e imprime
lista_coisas = list(coisas)
print(lista_coisas)
