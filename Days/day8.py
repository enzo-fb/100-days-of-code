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
    
dados = {'nome':'Pedro', 'idade':23}

for chave in dados.values():
    print(chave)
    
for chave in dados.keys():
    print(chave)
    
for chave in dados.items():
    print(chave)
    
print(dados.get('nome'))
print(dados.get('idade'))

dados.update({'idade': 25})
print(dados)
             
del dados["idade"]
print(dados)

dados.pop('nome')
print(dados)
