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

#cria varias fatias e junta tudo em uma nova lista
def dividir_lista(lista, tamanho):
    return [lista[i:i+tamanho] for i in range(0, len(lista), tamanho)]

printar_frutas(dividir_lista(frutas,2))

############ TUPLAS #################
coisas = ('carro', 23, True, 1.87, ' rapido')

print(coisas[3])
print(coisas[0] +coisas[4]*2)
print('carro' in coisas)

lista_coisas = list(coisas)
print(lista_coisas)