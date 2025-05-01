# Definição dos conjuntos
conjunto = {1, 2, 2, 4, 6, 3, 3}
conjunto2 = {33, 233, 5, 56}

# Exibindo o conjunto inicial
print("Conjunto inicial:", conjunto)

# Adicionando um elemento ao conjunto
conjunto.add(10)
print("Após adicionar 10:", conjunto)

# Removendo um elemento do conjunto
conjunto.remove(1)
print("Após remover 1:", conjunto)

# União dos conjuntos
uniao_conjunto = conjunto.union(conjunto2)
print("União dos conjuntos:", uniao_conjunto)

# Diferença entre os conjuntos
diferenca_conjunto = conjunto.difference(conjunto2)
print("Diferença dos conjuntos:", diferenca_conjunto)

# Iterando sobre os elementos do conjunto
print("Elementos do conjunto:")
for elemento in conjunto:
    print(elemento)

# Trabalhando com dicionários
dados = {'nome': 'Pedro', 'idade': 23}

# Iterando sobre os valores do dicionário
print("Valores do dicionário:")
for valor in dados.values():
    print(valor)

# Iterando sobre as chaves do dicionário
print("Chaves do dicionário:")
for chave in dados.keys():
    print(chave)

# Iterando sobre os itens do dicionário
print("Itens do dicionário:")
for item in dados.items():
    print(item)

# Acessando valores específicos
print("Nome:", dados.get('nome'))
print("Idade:", dados.get('idade'))

# Atualizando o dicionário
dados.update({'idade': 25})
print("Dicionário atualizado:", dados)

# Removendo elementos do dicionário
del dados["idade"]
print("Após remover 'idade':", dados)

dados.pop('nome')
print("Após remover 'nome':", dados)
